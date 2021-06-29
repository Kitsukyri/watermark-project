from PIL import Image, ImageDraw, ImageFont

def my_watermark(filename, message):
    im = Image.open(filename)
    im.save(filename + "_wm")

my_watermark(filename, message)