# import os
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from googleapiclient.http import MediaFileUpload
#
# #5. Set up the credentials by creating a credentials object:
#
# SCOPES = ['https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = 'credentials.json'
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#
# #6. Create a Drive API client by using the build() method:
#
# service = build('drive', 'v3', credentials=credentials)
#
# #7. Set the file path of the image you want to upload:
#
# file_path = 'R.jpg'
#
# #8. Create a MediaFileUpload object for the image file:
#
# file_metadata = {'name': os.path.basename(file_path),
#                  'parents': 'IMAGE',}
# media = MediaFileUpload(file_path, resumable=True)
#
# #9. Upload the image to Google Drive using the files().create() method:
#
# file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
# if file:
#     print(f'File ID: {file.get("id")}')
# else:
#     print('upload failed')
"""******************************
*******************************
# ***************************************************************************"""
# import io
#
# from pydrive.auth import GoogleAuth
# import os
# import json
# import requests
#
# url = 'R.jpg'
# filename = 'AAAAAAAAAAAAAAAAA'
# folder_id = 'root'
#
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
#
# metadata={
#     "name" : filename,
#     "parents" : [folder_id]
# }
# files = {
#     'data':('metadata', json.dumps(metadata),'application/json'),
#     'file':io.BytesIO(url)
# }
#
# r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#                   headers={"Authorization":"Bearer "+gauth.credentials.access_token},
#                   files=files)
"""*************************************
*************************************************
*************************************************************************"""



