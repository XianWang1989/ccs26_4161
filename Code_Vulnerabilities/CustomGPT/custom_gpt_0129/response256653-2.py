
from PIL import features

# Check if JPEG support is available
print("Jpeg support:", features.check("jpeg"))  # Should return True if available
