
from PIL import Image

# Check if JPEG is supported
print("JPEG support:", "JPEG" in Image.registered_extensions())
