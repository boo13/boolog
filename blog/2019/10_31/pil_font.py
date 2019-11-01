from os import listdir
from PIL import ImageFont, ImageDraw, Image

image = Image.open("image.png")
print(image.format)
print(image.mode)
print(image.size)


draw = ImageDraw.Draw(image)

# use a truetype font
font = ImageFont.truetype("FiraCode-Medium.ttf", size=24, )

draw.text((10, 25), "world", font=font)

image.show()
