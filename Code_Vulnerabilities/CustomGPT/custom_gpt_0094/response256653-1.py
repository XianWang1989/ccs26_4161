
from PIL import Image

# Check if JPEG support is available
try:
    img = Image.open("example.jpg")
    img.verify()  # Verify the image is okay
    print("JPEG support is working!")
except Exception as e:
    print(f"JPEG support is not working: {e}")
