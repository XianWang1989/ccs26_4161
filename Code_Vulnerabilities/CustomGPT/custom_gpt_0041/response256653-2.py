
from PIL import Image

try:
    img = Image.open('sample.jpg')
    img.show()
except IOError:
    print("JPEG support is not available. Cannot open JPEG images.")
