
from PIL import Image

# Create a sample JPEG image
image = Image.new("RGB", (100, 100), color=(155, 0, 0))
image.save("sample.jpg")

# Try opening and verifying the created JPEG image
try:
    img = Image.open("sample.jpg")
    img.verify()
    print("JPEG support is working!")
except Exception as e:
    print(f"JPEG support not working: {e}")
