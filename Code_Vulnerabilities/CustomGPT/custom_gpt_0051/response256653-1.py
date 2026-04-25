
from PIL import Image

# Check if JPEG is available
try:
    img = Image.open('test.jpg')
    img.verify()  # Verify that it is a valid image
    print("JPEG support is working.")
except (IOError, SyntaxError) as e:
    print("JPEG support is NOT working.")
