
from PIL import Image

print("Pillow version:", Image.__version__)
print("JPEG support:", "JPEG" in Image.core.__dict__)
