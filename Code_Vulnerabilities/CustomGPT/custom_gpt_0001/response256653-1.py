
from PIL import Image

# Replace 'sample.jpg' with your JPEG file name
try:
    img = Image.open('sample.jpg')
    img.show()
    print("JPEG support is working!")
except ImportError:
    print("Pillow is not installed, or JPEG support is missing.")
except Exception as e:
    print(f"An error occurred: {e}")
