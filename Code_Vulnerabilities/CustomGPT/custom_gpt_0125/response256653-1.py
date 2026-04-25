
from PIL import Image

try:
    image = Image.open('test.jpg')
    print("JPEG support is working!")
except IOError:
    print("JPEG support is NOT working!")
