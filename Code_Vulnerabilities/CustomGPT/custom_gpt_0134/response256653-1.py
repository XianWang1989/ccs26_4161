
from PIL import Image

try:
    # Attempt to open a JPEG image
    img = Image.open("example.jpg")
    img.show()
    print("JPEG support is working!")
except IOError:
    print("Unable to open JPEG image. JPEG support may not be installed.")
