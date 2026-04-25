
from PIL import Image

try:
    img = Image.open("test.jpg")  # Make sure you have a test.jpg file in the same directory
    img.verify()  # Will not load the image, just check if it's valid
    print("JPEG support works!")
except Exception as e:
    print("JPEG support not implemented:", e)
