
from PIL import Image

# Try opening a JPEG file
try:
    img = Image.open("test.jpg")  # Replace with an actual JPEG file path
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
