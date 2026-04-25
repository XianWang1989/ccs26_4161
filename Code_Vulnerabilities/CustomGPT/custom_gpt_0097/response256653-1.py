
from PIL import Image

try:
    img = Image.open("your_image.jpg")  # Replace with an actual JPEG file
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print("JPEG support is not working:", e)
