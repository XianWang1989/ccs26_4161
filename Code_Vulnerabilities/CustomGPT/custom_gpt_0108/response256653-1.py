
from PIL import Image

try:
    img = Image.open("example.jpg")
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
