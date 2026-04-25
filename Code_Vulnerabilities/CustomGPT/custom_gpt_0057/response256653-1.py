
from PIL import Image

try:
    img = Image.open('test.jpg')
    img.show()
    print("JPEG file opened successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
