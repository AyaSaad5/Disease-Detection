import firebase_admin
from firebase_admin import credentials , storage
from firebase_admin import firestore


def GetImageUrl(WantedImage , i):
    cred = credentials.Certificate("agriculture-project-691c0-firebase-adminsdk-7z0uf-1eccee64a4.json")
    firebase_admin.initialize_app(cred, {'storageBucket': 'agriculture-project-691c0.appspot.com'})
# # 2 -initialize the firestore instance.
#     db = firestore.client()

    bucket = storage.bucket()
    token = bucket.generate_signed_url(expiration=36000 , method='GET')
    blob = bucket.blob(WantedImage)
    print(blob.path)

    # url = blob.path
    # print(token)
    # print(url)

    u = f'https://firebasestorage.googleapis.com/v0/b/agriculture-project-691c0.appspot.com/o/data%2Fphoto{i}.jpg?alt=media&token='+token
    print(u)
    return u
# https://storage.googleapis.com/agriculture-project-691c0.appspot.com/UploadedImage

# print(u)