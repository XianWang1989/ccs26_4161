
from PIL import Image

try:
    img = Image.open("test.jpg")  # Make sure there is a test.jpg file in the same directory
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not working.")
