
from PIL import Image

# Attempt to open a JPEG image
try:
    img = Image.open('sample.jpg')  # Ensure 'sample.jpg' exists in the same directory
    img.show()  # This should display the image if JPEG support is working
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
