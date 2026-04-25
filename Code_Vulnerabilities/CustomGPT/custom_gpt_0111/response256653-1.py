
from PIL import Image

# Attempt to open a JPEG image
try:
    img = Image.open('example.jpg')
    img.show()
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not available.")
