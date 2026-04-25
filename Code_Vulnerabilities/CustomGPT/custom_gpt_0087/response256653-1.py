
from PIL import Image

# Try opening a JPEG file
try:
    img = Image.open("sample.jpg")
    img.show()
except IOError:
    print("JPEG support not available.")
