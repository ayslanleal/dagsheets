from __future__ import print_function

import os.path
from venv import create
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



class Service:

    def create_service(self,scope,field, version):
        """Shows basic usage of the Google API microsservice. 
        Instance of Google api.
        """
        self.scope = scope
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.scope)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scope)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build(f'{field}', f'{version}', credentials=creds)
            return service
        except HttpError as error:
            
            print(f'An error occurred: {error}')

class Drive(Service):
    
    """
    Instance of Drive API
    """
    def create_service(self):
        return super().create_service(['https://www.googleapis.com/auth/drive'], 'drive', 'v3')

class Sheets(Service):
    
    """
    Instance of Drive API
    """
    def create_service(self):
        return super().create_service(['https://www.googleapis.com/auth/spreadsheets'], 'sheets', 'v4')

