
from PIL import Image

try:
    img = Image.open('test.jpg')
    img.show()
except Exception as e:
    print(f"Error: {e}")
