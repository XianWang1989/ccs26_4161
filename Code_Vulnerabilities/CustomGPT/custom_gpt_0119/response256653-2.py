
from PIL import Image

try:
    img = Image.open('example.jpg')  # Replace with a valid JPEG file
    img.show()
except IOError:
    print("JPEG support is not available.")
