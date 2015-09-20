from PIL import Image
import tempfile
"""
beginning and end are keypoints and imagePath is the name/path of the image
For easy processing of sidebar
"""
def getMarkupTab(imagePath):
    #fallback
    marginSize = 200
    image = imagePath
    original = Image.open(image)
    width,height = original.size
    left = 0
    top = 0
    rgb  =  original.convert('RGB')
    for x in range(0,width/3):
        r,g,b = rgb.getpixel((x,0))
        if (g < 145):
            marginSize = x
    if width< marginSize:
        marginSize = width
    print marginSize
    right = marginSize
    bottom = height
    cropped_example = original.crop((left,top, right, bottom))
    tempFileName = tempfile.NamedTemporaryFile().name +".jpg"
    cropped_example.save(tempFileName)
    # cropped_example.show()
    return tempFileName
