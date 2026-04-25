
from PIL import Image

# Try to open a JPEG file
try:
    img = Image.open("example.jpg")
    img.show()
except Exception as e:
    print(f"Error opening JPEG: {e}")
