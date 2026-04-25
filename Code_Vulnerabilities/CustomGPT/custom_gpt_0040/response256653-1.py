
from PIL import Image

try:
    im = Image.open("example.jpg")
    print("JPEG image opened successfully!")
    im.show()
except Exception as e:
    print(f"Failed to open JPEG image: {e}")
