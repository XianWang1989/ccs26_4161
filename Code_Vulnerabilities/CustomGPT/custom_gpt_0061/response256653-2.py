
from PIL import Image

# Test opening a JPEG image
try:
    img = Image.open("test_image.jpg")  # Replace with a valid JPEG file path
    img.show()  # Opens the image
    print("Image mode:", img.mode)  # Should print 'RGB' for a JPEG
    print("Image size:", img.size)  # Prints the dimensions of the image
except IOError:
    print("Failed to open image. JPEG support may not be installed.")
