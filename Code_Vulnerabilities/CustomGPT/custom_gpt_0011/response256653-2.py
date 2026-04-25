
from PIL import Image

# Open a JPEG file
try:
    img = Image.open("example.jpg")  # Replace 'example.jpg' with the path to your JPEG file
    print("Image format:", img.format)
    print("Image size:", img.size)
    img.show()
except IOError:
    print("Unable to open image file.")
