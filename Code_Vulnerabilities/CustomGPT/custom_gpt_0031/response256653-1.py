
from PIL import Image

# Try to open an existing JPEG file
try:
    img = Image.open('example.jpg')  # Replace with a valid JPEG file path
    img.show()  # Should display the image without errors
except IOError:
    print("JPEG support is not enabled.")
