
from PIL import Image

# Test if opening a JPEG image works
try:
    img = Image.open("your_image.jpg")  # Replace 'your_image.jpg' with an actual file path
    img.show()
except IOError:
    print("Unable to open JPEG image.")
