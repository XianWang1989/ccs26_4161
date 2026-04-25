
from PIL import Image

# Open an existing JPEG image
try:
    img = Image.open('example.jpg')
    img.show()
    print("JPEG image opened successfully!")
except IOError:
    print("Unable to open JPEG image.")
