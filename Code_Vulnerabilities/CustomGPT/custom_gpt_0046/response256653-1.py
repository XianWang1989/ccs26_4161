
from PIL import Image

try:
    img = Image.open('example.jpg')  # Make sure example.jpg exists
    img.show()
except IOError:
    print("JPEG support not available.")
