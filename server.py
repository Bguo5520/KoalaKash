from flask import Flask
app = Flask('barone')
import os.path
import pickle
@app.route('/KoalaKash')
def hello_world():
    return 'Hello, World!' 
from google.auth.transport.requests import Request

from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.oscom/auth/spreadsheets'
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)


service = discovery.build('sheets', 'v4', credentials=creds)

# The ID of the spreadsheet to update.
spreadsheet_id = '1rcnd-cIu4xMOuQN-EyUvHPWICxlmOSnC2qlhiqaZpF4'  # TODO: Update placeholder value.

# The A1 notation of the values to update.
range_name = 'A2:B5'  # TODO: Update placeholder value.

result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()

values = result.get('values')
print values