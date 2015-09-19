from PIL import Image
image = "image.jpg"
original = Image.open(image)
original.show()
width,height = original.size
left = width/4
top = height/4
right = 3*width/4
bottom = 3*height/4
cropped_example = original.crop((left,top, right, bottom))
cropped_example.show()
