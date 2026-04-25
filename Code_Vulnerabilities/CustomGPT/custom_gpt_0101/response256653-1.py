
from PIL import Image

# Test opening a JPEG image
try:
    img = Image.open("test.jpg")
    img.show()
except Exception as e:
    print(f"Error opening JPEG: {e}")
