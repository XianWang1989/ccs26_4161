
from PIL import Image

# Replace 'example.jpg' with your JPEG file path
try:
    img = Image.open('example.jpg')
    img.show()  # This will open the image in the default viewer
except IOError:
    print("Cannot open the image. JPEG support may not be installed.")
