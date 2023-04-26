import firebase_admin
from firebase_admin import credentials , storage
from firebase_admin import firestore

def uploadImage(imagename):

    # cred = credentials.Certificate("agriculture-project-691c0-firebase-adminsdk-7z0uf-1eccee64a4.json")
    # firebase_admin.initialize_app(cred, {'storageBucket': 'agriculture-project-691c0.appspot.com'})
    # # 2 -initialize the firestore instance.
    # db = firestore.client()

    bucket = storage.bucket()
    token = bucket.generate_signed_url(expiration=36000 , method='GET')
    blob = bucket.blob('UploadedImage')
    blob.upload_from_filename(imagename)

    # url = blob.path
    # print(token)
    # print(url)

    u = 'https://firebasestorage.googleapis.com/v0/b/agriculture-project-691c0.appspot.com/o/UploadedImage?alt=media&token='+token
    return u
# https://storage.googleapis.com/agriculture-project-691c0.appspot.com/UploadedImage

# print(u)