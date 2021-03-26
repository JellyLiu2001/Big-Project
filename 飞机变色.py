from PIL import Image
im = Image.open("C:\\Users\\Jelly Jinzhe Liu\\Desktop\\a872c6cf49cf9562c9ae8444c667241.jpg")
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        print(r,g,b)