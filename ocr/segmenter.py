from blobdetection import Landmark
import blobdetection
import cropmarkup
import cropsection
imagePath = "blob.jpg"
sidePath = cropmarkup.getMarkupTab(imagePath)
landmarks = blobdetection.getLandmarks(sidePath)
for x in range(0, len(landmarks)):
    cropsection.getSection(landmarks[x].point, landmarks[x+1].point, imagePath)
    pdb.set_trace()
    if (x+1 == landmarks.count):
        break
