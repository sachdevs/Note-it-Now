from PIL import Image
import pdb
from cv2 import KeyPoint
import uuid
"""
beginning and end are keypoints and imagePath is the name/path of the image
"""
factor = 3
def getSection(beginning, end, imagePath):
    image = imagePath
    original = Image.open(image)
    width,height = original.size
    left = 0
    if beginning.pt[1]-beginning.size < 0 :
        top = beginning.pt[1]
    else:
        top = beginning.pt[1]-beginning.size * factor
    right = width
    if end == 0:
        bottom = height
    else:
        bottom = end.pt[1]+end.size*factor
    cropped_example = original.crop((int(left),int(top), int(right), int(bottom)))
    tempFileName = "static/temp/"+str(uuid.uuid4())+ ".jpg"
    cropped_example.save(tempFileName)
    # cropped_example.show()
    return tempFileName
