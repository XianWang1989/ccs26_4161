
from PIL import Image

# Check if Pillow can open JPEG images
try:
    img = Image.open("example.jpg")
    img.show()
    print("JPEG support is working.")
except Exception as e:
    print("JPEG support is not available:", e)
