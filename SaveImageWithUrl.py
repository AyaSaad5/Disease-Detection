import urllib.request
def GetImage(url ,currentPath ):
    # imgURL = "https://firebasestorage.googleapis.com/v0/b/agriculture-project-691c0.appspot.com/o/data%2Fphoto.jpg?alt=media&token=https://storage.googleapis.com/agriculture-project-691c0.appspot.com?Expires=36000&GoogleAccessId=firebase-adminsdk-7z0uf%40agriculture-project-691c0.iam.gserviceaccount.com&Signature=SE5NGIgIWLkTC7ieNES9P0f5UvQuSmxP10WYezZlJnwmsOWRGl79tf8z1pf2RZOl8NXKpcZwVH7x8%2Bxg5fMRnOlw8feccQaiA5QHi5pMi8rJ6ZmhwaOOHQLq%2FlsAb6WKSey%2FOmao69eMZYR3HwOxMaL991mXXybyZwwgduoSG%2B2uU5JHnAmQnzYH72xWow9xN%2BRvEgTOiSwR4jKA0lDAaHB%2FUrmYAfWJ%2Bpt%2FkfCvasoo%2B9%2FfnvIETd1V5SkRgyAU517Jib1PdEeFqgHBvPsUy4CIPlbFcmDtWyA8sVuaaGPXOs62j%2F%2F30qDXRtdhHRxiHD%2FFBtqkn2A1C65Gc3WinQ%3D%3D"
    # currentPath = "E:/local-filename.jpg"
    urllib.request.urlretrieve(url,currentPath)

    return currentPath
