
from PIL import Image

if 'jpeg' in Image.EXTENSION:
    print("JPEG support is available!")
else:
    print("JPEG support is not available.")
