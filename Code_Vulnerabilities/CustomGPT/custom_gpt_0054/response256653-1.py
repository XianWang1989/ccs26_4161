
from PIL import Image

# Try opening a JPEG image
try:
    img = Image.open('example.jpg')  # Replace with the path to your JPEG file
    img.show()  # This should open the image if successful
except IOError:
    print("Cannot open JPEG file. Please check the installation and libraries.")
