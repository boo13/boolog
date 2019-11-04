from PIL import Image, ImageDraw, ImageFont
from loguru import logger
import os
import glob

size = (700, 300)
bkg_color = (73, 109, 137)
text_color = (255, 255, 0)
output_text_color = (255, 255, 255)
X_PAD = 20
Y_PAD = 30

font_size = 18
fnt = ImageFont.truetype('/Library/Fonts/FiraCode-Medium.ttf', font_size)


def make_image(input_text="Hello World 1234567890 1234567890 1234567890 1234567890", output_text="Output"):
    img = Image.new('RGB', size=size, color=bkg_color)

    text_to_write = "> " + input_text
    out_text_to_write = "  " + output_text
    logger.debug(f"(Text letter count: {len(input_text)})")

    d = ImageDraw.Draw(img)
    # d.text((X_PAD, Y_PAD + Y_PAD), out_text_to_write, font=fnt, fill=output_text_color)

    x_pos = 0
    image_list = []

    for n, t in enumerate(text_to_write):
        d.text((X_PAD + x_pos, Y_PAD), text_to_write[n], font=fnt, fill=text_color)
        #
        name = f'pil_text_font_{str(n).zfill(4)}.gif'
        image_list.append(name)
        img.save(name)
        x_pos += 12



    image_list[0].save('anicircle.gif',
                   save_all=True,
                   append_images=image_list[1:],
                   duration=100,
                   loop=0)


    # return image_list

def load_images_from_folder(folder="."):
    image_list = []

    for filename in glob.glob(f'{folder}/*.gif'):
        frame = Image.open(filename)
        logger.debug(filename)
        if frame is not None:
            image_list.append(frame)
    return sorted(image_list)


def make_gif():
    frames = load_images_from_folder()
    # Save the frames as an animated GIF
    frames[0].save('anicircle.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=100,
                   loop=0)



if __name__ == "__main__":
    make_image()
    # make_gif()