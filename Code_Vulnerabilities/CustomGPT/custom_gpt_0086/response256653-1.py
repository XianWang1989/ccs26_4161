
from PIL import Image

try:
    img = Image.open("test.jpg")  # Replace 'test.jpg' with a sample JPEG image path
    img.verify()  # Verifies the image
    print("JPEG support is working!")
except (IOError, SyntaxError) as e:
    print("JPEG support is NOT working!")
