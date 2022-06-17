from datetime import datetime, timedelta
import io
from auth.Google import Drive, Sheets
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload  
import os
import pandas as pd

class DriveService():
    def __init__(self):
        self.drive_service = Drive().create_service()

    def get_fold_id(self):
        page_token=None
        self.get_fold = self.drive_service.files()\
            .list(
                q="mimeType = 'application/vnd.google-apps.folder'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token
            ).execute()
        
        for values_response in self.get_fold.values():
            for v in values_response:
                if v['name'] == 'Case Data Eng Jr. 2022':
                    return v['id']
    
    def get_file_id(self):
        self.get_file = self.drive_service.files() \
            .list(
                q=f"parents = '{self.get_fold_id()}'"
            ).execute()
        for i in self.get_file['files']:
            return i['id']

    def get_media(self):
        self.get_media = self.drive_service.files() \
            .get_media(
                fileId=self.get_file_id()
            )
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=self.get_media)

        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        fh.seek(0)

        df = pd.read_json(io.BytesIO(fh.read()))
        
        return df

    def get_fold_modifier(self):
        page_token = None
        yesterday = str((datetime.today()-timedelta(days=5)).strftime('%Y-%m-%d')+'T'+'00:00:00')
        while True:
            response = self.drive_service.files().list(q=f"modifiedTime > '{yesterday}'",
                                                spaces='drive',
                                                fields='nextPageToken, files(id, name)',
                                                pageToken=page_token).execute()

            file_id = self.get_file_id()                                 
            for file in response.get('files', []):
                if file_id == file.get('id'):
                    return True

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                return False
            
        

class SheetsSevice():
    def __init__(self, df):
        self.sheet_service = Sheets().create_service()
        self.spreedsheet_id = '1UlY-tUUTTX_PfXd19wSJ_S2-CcYb8rj5sukpf1UfGt4'
        self.df = df

    def update_sheets(self):
        self.update = self.sheet_service.spreadsheets().values() \
            .update(
                spreadsheetId=self.spreedsheet_id, 
                range='sheets1',
                valueInputOption='RAW'
                ,body={'values': [self.df.columns.values.tolist()] + self.df.values.tolist()}
                ).execute()
        print("File updated !")
    

    
if __name__ == '__main__':
    drive = DriveService()
    sheet = SheetsSevice(drive.get_media())
    if drive.get_fold_modifier():
        sheet.update_sheets()
    else:
        print("Nos ultimos 5 dias não houve modificação!")

