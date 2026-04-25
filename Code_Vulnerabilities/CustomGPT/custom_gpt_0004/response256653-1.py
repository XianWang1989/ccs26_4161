
from PIL import Image
print("Pillow version:", Image.__version__)
print("JPEG support:", "jpeg" in Image.SUPPORTED_FORMATS)  # Should return True if JPEG is supported
