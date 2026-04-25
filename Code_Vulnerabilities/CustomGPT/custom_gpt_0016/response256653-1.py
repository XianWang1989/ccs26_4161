
from PIL import Image

# Attempt to open a JPEG file
try:
    img = Image.open("sample.jpg")  # Replace with your JPEG file path
    img.show()  # This opens the image with the default image viewer
    print("JPEG support is working!")
except Exception as e:
    print("Failed to open JPEG file:", e)
