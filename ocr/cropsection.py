from PIL import Image
"""
beginning and end are keypoints and imagePath is the name/path of the image
"""
def getSections(beginning, end, imagePath):
    image = imagePath
    original = Image.open(image)
    width,height = original.size
    left = beggining.pt.x
    top = beggining.pt.y
    right = width
    bottom = end.pt.y
    cropped_example = original.crop((left,top, right, bottom))
    cropped_example.save(imagePath+".edited")
    cropped_example.show()
