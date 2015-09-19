from PIL import Image
"""
beginning and end are keypoints and imagePath is the name/path of the image
For easy processing of sidebar
"""
marginSize = 200
def getMarkupTab(imagePath):
    image = imagePath
    original = Image.open(image)
    width,height = original.size
    left = 0
    top = 0
    rgb  =  original.convert('RGB')
    for x in range(0,width/3):
        r,g,b = rgb.getpixel((x,0))
        if (g < 160):
            marginSize = x
    print marginSize
    right = marginSize
    bottom = height
    cropped_example = original.crop((left,top, right, bottom))
    cropped_example.save(imagePath+".sidebar.jpg")
    cropped_example.show()
# getMarkupTab("landscapebinder.png")
