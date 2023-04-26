import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from setuptools.command.saveopts import saveopts

import TestUploadingImageToStorage
import DownloadingImageFromStorage
import SaveImageWithUrl
import time
import pyfirmata
import ultralytics
from ultralytics import YOLO
import os
import cv2



i=2
ImageStoragePath = DownloadingImageFromStorage.GetImageUrl(f"data/photo{i}.jpg" , i)
ImageLocalPath = SaveImageWithUrl.GetImage(ImageStoragePath,f"E:/photo{i}.jpg")
print(ImageStoragePath)
print(ImageLocalPath)


os.chdir(r"E:/")
diseaseName = " "
model = YOLO("best (2).pt")
results = model.predict(source=ImageLocalPath, show=True, conf=0.25 , save =True )
for r in results:
    for c in r.boxes.cls:
        m = model.names[int(c)]
        diseaseName=m

                                                                                                                # cv2.imwrite("E:/T2.jpg",results)
print(m)
# cv2.waitKey(0)

# # 1 -initialize the SDK using our downloaded service account credentials.
# cred = credentials.Certificate("agriculture-project-691c0-firebase-adminsdk-7z0uf-1eccee64a4.json")
# firebase_admin.initialize_app(cred, {'storageBucket': 'agriculture-project-691c0.appspot.com'})
# # 2 -initialize the firestore instance.
db = firestore.client()


# # #  image path in drive
# # path = "https://drive.google.com/file/d/1nSspmP9NxHmsjkWtFFJv73QPkigfoZwj/view?usp=sharing"
# # path1 = "https://drive.google.com/file/d/1tXKRNvuNQWIyp08EQqVLk5YN-uyiyFDK/view?usp=sharing"
# # # splitting path to get image's id
# # list = path.split("/")
# # print(list)
# # print(list[5])
# # imageId = list[5]
# # newPath = f"https://drive.google.com/uc?export=view&id={imageId}"
#
#
newPath = TestUploadingImageToStorage.uploadImage(f'runs/detect/predict/photo{i}.jpg')
print(newPath)
# diseaseName=m

obj={
    'Image':newPath,
    'Name':diseaseName
    }

# 3 -get the document from our collection. For that, we’ll use .update() method.
doc_ref = db.collection('DiseaseClassification').document('EWMTBLmvC2zG3sY5FyPG')
doc_ref.update(obj)
