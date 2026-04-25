
from PIL import Image

# Create a simple image
image = Image.new("RGB", (100, 100), color=(255, 0, 0))

# Save the image as a JPEG
image.save("test_image.jpg", "JPEG")

# Open the JPEG image
try:
    img = Image.open("test_image.jpg")
    img.show()  # This will open the image if the decoder is working
except IOError:
    print("JPEG support is still not installed!")
