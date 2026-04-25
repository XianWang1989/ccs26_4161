
from PIL import Image

# Create a new image (RGB mode) and save as JPEG
image = Image.new('RGB', (100, 100), color = 'blue')
image.save('test_image.jpg')

# Attempt to open and show the image
try:
    img = Image.open('test_image.jpg')
    img.show()
except IOError:
    print("Unable to open or manipulate JPEG images. Check Pillow installation.")
