
from PIL import Image

try:
    img = Image.open('path_to_your_image.jpg')  # Replace with your JPEG file path
    img.show()  # This should open the image
except IOError:
    print("Cannot open JPEG file. JPEG support may not be installed.")
