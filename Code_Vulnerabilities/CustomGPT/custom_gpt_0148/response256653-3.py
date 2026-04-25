
from PIL import Image

# Test with an example JPEG file
try:
    img = Image.open("example.jpg")  # Replace with your JPEG file
    img.show()  # Should open the image if JPEG support is working
    print("Successfully opened JPEG image.")
except Exception as e:
    print(f"Failed to open JPEG image: {e}")
