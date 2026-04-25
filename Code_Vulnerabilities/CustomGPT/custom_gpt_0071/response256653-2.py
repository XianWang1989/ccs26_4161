
from PIL import Image, ImageDraw

# Create a new JPEG image
def create_jpeg_image(filename):
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Hello", fill=(255, 255, 0))

    img.save(filename, "JPEG")
    print(f"{filename} created successfully.")

# Test function
create_jpeg_image("test.jpg")

# Verify JPEG support
try:
    img = Image.open("test.jpg")
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not working.")
