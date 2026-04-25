
from PIL import Image

# Check if JPEG support is available
if 'jpeg' in Image.registered_extensions():
    print("JPEG support is installed!")
else:
    print("JPEG support is NOT installed.")
