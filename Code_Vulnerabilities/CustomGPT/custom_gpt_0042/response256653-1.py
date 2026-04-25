
from PIL import Image

# Try opening a JPEG image
try:
    img = Image.open("test.jpg")
    img.show()  # This should open the image if supported
    print("JPEG support is working!")
except IOError:
    print("JPEG support is NOT working.")
