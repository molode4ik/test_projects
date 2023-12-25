import os

cwd = os.getcwd()
secret_keys = os.path.join(cwd, 'secret_keys')
SECRET_PATH = os.path.join(secret_keys, 'testproject-409111-8cf46d41a01f.json')
DOCUMENT_URL = 'https://docs.google.com/spreadsheets/d/1Aojy-Z_SLzp965f-pROxVPq-LaqKOMVnXRt8dgGuvwY/edit#gid=0'
HOST = '0.0.0.0'
PORT = 7000