
from PIL import Image, ImageDraw, ImageFont

# Create an image
img = Image.new('RGB', (200, 100), color='white')
d = ImageDraw.Draw(img)

# Use a built-in font
font = ImageFont.load_default()
d.text((10, 10), "Hello World!", fill="blue", font=font)

# Save the image
img.save('styled_text.png')
