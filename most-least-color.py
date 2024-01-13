# conda activate iWM

# pip install colorthief

from colorthief import ColorThief
from PIL import Image, ImageDraw

from draw_multiline_text import text_color


name = 't1.PNG'


color_thief = ColorThief(name)
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)


# print("dominant_color = ", dominant_color)
# print("least_color = ", palette[-1])

# img = Image.new('RGB', (500, 300), dominant_color)
# draw = ImageDraw.Draw(img)

# draw.rectangle(
#    (200, 125, 300, 200),
#    fill=palette[-1],
#    outline=(0, 0, 0))

# img.save(f'most-least-{name[:-4]}.png')
# img.show()


text_color(f"colored_text_for_{name[:-4]}.jpg", dominant_color, palette[-1])