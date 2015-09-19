from PIL import Image
import pdb
from cv2 import KeyPoint
"""
beginning and end are keypoints and imagePath is the name/path of the image
"""
def getSection(beginning, end, imagePath):
    image = imagePath
    original = Image.open(image)
    width,height = original.size
    left = 0
    if beginning.pt[1]-beginning.size < 0 :
        top = beginning.pt[1]
    else:
        top = beginning.pt[1]-beginning.size
    right = width
    if end == 0:
        bottom = height
    else:
        bottom = end.pt[1]
    cropped_example = original.crop((int(left),int(top), int(right), int(bottom)))
    cropped_example.save(imagePath+".edited.png")
    cropped_example.show()
    return imagePath + ".edited.png"
# getSections(KeyPoint(0, 0, 10),KeyPoint(0, 100,10),"landscapebinder.png")
