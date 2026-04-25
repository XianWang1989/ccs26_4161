
from PIL import Image

try:
    # Attempt to open a jpg image
    img = Image.open('test.jpg')
    img.show()
    print("JPEG image opened successfully.")
except IOError:
    print("JPEG support is not working.")
