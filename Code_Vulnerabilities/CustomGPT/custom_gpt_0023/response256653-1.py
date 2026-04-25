
from PIL import Image

try:
    img = Image.open('test.jpg')  # Replace with an actual JPEG file path
    img.load()
    print("JPEG support is working!")
except Exception as e:
    print(f"An error occurred: {e}")
