
from PIL import Image

# Check if JPEG support is available
print("JPEG support:", "jpeg" in Image.registered_extensions())
