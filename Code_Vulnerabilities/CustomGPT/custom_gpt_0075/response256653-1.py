
from PIL import Image

# Attempt to open a JPEG file
try:
    img = Image.open('example.jpg')
    img.show()
except Exception as e:
    print(f"Error: {e}")
