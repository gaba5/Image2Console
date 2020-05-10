from colr import color
from PIL import Image
import numpy


def string_image(path, size=100):
    image_type=path.split("/")[-1].split(".")[-1]
    if image_type!='jpg':
        return color(f'Image2console Error: Please enter a image type of jpg not "{image_type}"', fore=(200, 0, 0), back=0)

    if size>100:
        size=100
    def rgb2pix(rgb):
        return color('  ', fore=rgb, back=rgb)

    def get_image_data(image_path):
        image = Image.open(image_path, 'r')
        image=image.resize((size,size))
        pixel_values = list(image.getdata())
        if image.mode == 'RGB':
            channels = 3
        elif image.mode == 'L':
            channels = 1
        else:
            return color(f'Unknown File Mode {image.mode}', fore=(200,0,0), back=0)
        pixel_values = numpy.array(pixel_values).reshape((size, size, channels))
        return pixel_values

    str_pic=""
    rgb_values=get_image_data(path)
    for row in range(size):
        for num,i in enumerate(rgb_values[row]):
            if num==size-1:
                pixel=f"{rgb2pix(list(i))}\n"
            else:
                pixel=rgb2pix(list(i))
            str_pic+=pixel
    return str_pic
