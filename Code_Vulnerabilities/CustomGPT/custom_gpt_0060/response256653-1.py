
from PIL import Image

try:
    img = Image.open("example.jpg")  # Use an actual JPEG file path
    img.verify()  # Verify that it is, in fact, a JPEG
    print("JPEG support is enabled!")
except Exception as e:
    print(f"JPEG support is not enabled: {e}")
