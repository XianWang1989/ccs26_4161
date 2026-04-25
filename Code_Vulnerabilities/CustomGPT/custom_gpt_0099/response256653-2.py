
from PIL import Image

# Load a JPEG image
try:
    img = Image.open("path_to_your_image.jpg")
    img.show()  # Opens the default image viewer
    print("Image format:", img.format)
except Exception as e:
    print("Failed to open image:", e)
