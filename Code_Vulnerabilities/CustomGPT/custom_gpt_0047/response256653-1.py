
from PIL import Image

try:
    img = Image.open("example.jpg")
    img.show()
except IOError:
    print("JPEG support is not available.")
