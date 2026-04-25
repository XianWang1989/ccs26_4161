
from PIL import Image
try:
    img = Image.open("sample.jpg")
    img.show()
    print("JPEG support is working.")
except Exception as e:
    print(f"Error: {e}")
