# https://www.blog.pythonlibrary.org/2021/02/02/drawing-text-on-images-with-pillow-and-python/

from PIL import Image, ImageDraw, ImageFont

def text(input_image_path, output_path):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("eliss.ttf", size=66)
    text = "TEST +7698541254\nTeXt + 9 5 4 6 8"
    color = (255, 102, 0)
    draw.text((10, 25), text, font=font, fill=color)
    image.save(output_path)

def text_color(output_path, color_back = (203, 72, 12), color_text = (154, 128, 110)):
    color_back = color_back
    color_text = color_text
    image = Image.new("RGB", (1280, 960), color_back)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("eliss.ttf", size=66)

    x = 15
    y = 10
    text = "+1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"

    draw.text((x, y), text, font=font, fill=color_text)
    image.save(output_path)

if __name__ == "__main__":
    # text("test1.jpg", "multiline_text_eliss.jpg")
    text_color("colored_text-for-eyes.jpg")