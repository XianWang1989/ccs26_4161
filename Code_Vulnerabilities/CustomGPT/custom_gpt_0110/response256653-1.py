
from PIL import Image

# Replace 'example.jpg' with the path to your JPEG file
try:
    img = Image.open('example.jpg')
    img.show()  # This will open the image in the default image viewer
except IOError:
    print("Unable to open the image. Ensure JPEG support is installed.")
