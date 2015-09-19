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
    # left = beginning.pt[0]
    left = 0
    top = beginning.pt[1]
    right = width
    bottom = end.pt[1]
    cropped_example = original.crop((int(left),int(top), int(right), int(bottom)))
    pdb.set_trace()
    cropped_example.save(imagePath+".edited.png")
    cropped_example.show()
    return imagePath + ".edited.png"
# getSections(KeyPoint(0, 0, 10),KeyPoint(0, 100,10),"landscapebinder.png")
