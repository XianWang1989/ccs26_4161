
from PIL import Image

# Attempt to open a JPEG file
try:
    img = Image.open("test.jpg")
    img.show()
except Exception as e:
    print(f"Failed to open JPEG image: {e}")
