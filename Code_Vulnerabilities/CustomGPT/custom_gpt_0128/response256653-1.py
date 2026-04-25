
from PIL import Image

# Try opening a JPEG file
try:
    img = Image.open("example.jpg")  # Make sure you have a sample JPEG file
    img.show()
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not working!")
