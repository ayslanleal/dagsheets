# 📝Dagsheets

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Projeto que simula um serviço de batch no Google Sheets utilizando arquivo de pasta compartilhada no Google Drive. 

[Link arquivo json][https://drive.google.com/drive/folders/1fdNuQje5ZUWrm3cWMPPDtypTkpgRwg3Q?usp=sharing]
[Link spreadsheet][https://docs.google.com/spreadsheets/d/1UlY-tUUTTX_PfXd19wSJ_S2-CcYb8rj5sukpf1UfGt4/edit?usp=sharing]

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Drive API](https://developers.google.com/drive)
- [Sheets API](https://developers.google.com/sheets/api)

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/), [Poetry][https://python-poetry.org/docs/#installation], [VSCode](https://code.visualstudio.com/).

Ademais você ira precisar de um arquivo de credenciais do app do google, mais informações em [Google Developers][https://developers.google.com/workspace/guides/get-started].
O arquivo .json das credenciais deverá ser salvo na pasta ./dagsheets como "credentials.json".

```bash
# Clone este repositório
$ git clone https://github.com/ayslanleal/dagsheets.git

# Acesse a pasta do projeto no terminal/cmd
$ cd dagsheets

# Inicicie o venv do projeto
$ poetry shell

# Instale as dependências
$ poetry install

# Vá para a pasta dagsheets
$ cd dagsheets

# Execute o script main.py
$ python main.py

```



