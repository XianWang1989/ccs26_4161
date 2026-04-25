
from PIL import Image

# Create a simple image and save it as JPEG
image = Image.new("RGB", (100, 100), color="red")
image.save("test_image.jpg")

# Try to open the JPEG image
try:
    img = Image.open("test_image.jpg")
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
