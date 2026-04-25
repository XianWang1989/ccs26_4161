
from PIL import Image

try:
    # Attempt to open a JPEG image
    img = Image.open('example.jpg')
    img.show()
except Exception as e:
    print(f"An error occurred: {e}")
