
from PIL import Image

# Try opening a JPEG file
try:
    img = Image.open("test.jpg")
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print("Error:", e)
