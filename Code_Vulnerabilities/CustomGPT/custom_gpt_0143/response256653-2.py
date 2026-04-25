
from PIL import Image

# Open a JPEG image file
try:
    img = Image.open('example.jpg')
    img.show()  # Display the image
except IOError:
    print("Unable to open image. JPEG support may not be available.")
