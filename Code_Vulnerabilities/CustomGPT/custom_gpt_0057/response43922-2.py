
from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (200, 100), color='white')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

text = "Hello, World!"
draw.text((10, 25), text, fill='blue', font=font)

image.save('text_image.png')
