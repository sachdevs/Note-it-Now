from blobdetection import Landmark
import blobdetection
import cropmarkup
import cropsection
import pdb
def getImages(filename):
    imagePath = filename
    sidePath = cropmarkup.getMarkupTab(imagePath)
    landmarks = blobdetection.getLandmarks(sidePath)
    landmarks.sort(key=lambda x: x.point.pt[1])
    imageArray = []
    for x in range(0, len(landmarks)):
        print x, len(landmarks)
        if (x+1 >= len(landmarks)):
            imageArray.append(cropsection.getSection(landmarks[x].point, 0, imagePath))
        else:
            imageArray.append(cropsection.getSection(landmarks[x].point, landmarks[x+1].point, imagePath))
    return imageArray
