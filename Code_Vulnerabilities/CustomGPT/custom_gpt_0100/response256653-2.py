
from PIL import Image

try:
    # Attempt to open a JPEG image
    img = Image.open("example.jpg")
    img.show()
    print("JPEG image opened successfully!")
except IOError:
    print("Failed to open JPEG image.")
