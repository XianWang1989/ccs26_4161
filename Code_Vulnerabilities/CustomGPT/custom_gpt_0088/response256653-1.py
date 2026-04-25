
from PIL import Image

# Check if JPEG loading is available
try:
    img = Image.open('test.jpg')  # Replace 'test.jpg' with a valid JPEG file path
    print("JPEG support is available!")
except IOError:
    print("JPEG support is NOT available.")
