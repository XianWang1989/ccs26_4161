
from PIL import Image

try:
    img = Image.open("test.jpg")
    img.verify()  # Will check if the image is valid
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
