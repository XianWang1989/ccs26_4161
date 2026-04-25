
from PIL import Image

# Check if JPEG support is available
if 'jpeg' in Image.registered_extensions().keys():
    print("JPEG support is available.")
else:
    print("JPEG support is NOT available.")
