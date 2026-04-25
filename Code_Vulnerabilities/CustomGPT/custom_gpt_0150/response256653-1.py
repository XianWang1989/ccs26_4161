
from PIL import Image

# Create a simple image
image = Image.new("RGB", (100, 100), (255, 0, 0))
image.save("test_image.jpg")

# Try to open the image back
try:
    img = Image.open("test_image.jpg")
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print(f"JPEG support is not working: {e}")
