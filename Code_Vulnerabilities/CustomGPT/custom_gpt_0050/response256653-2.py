
from PIL import Image

# Create an image and save as JPEG
image = Image.new("RGB", (100, 100), color=(255, 0, 0))
image.save("test_image.jpg", "JPEG")

# Open the saved JPEG image
try:
    jpeg_image = Image.open("test_image.jpg")
    jpeg_image.show()
    print("JPEG image opened successfully!")
except Exception as e:
    print(f"Failed to open JPEG image: {e}")
