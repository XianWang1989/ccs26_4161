
from PIL import Image

try:
    img = Image.open("test.jpg")
    img.show()
except IOError:
    print("JPEG support not available.")
