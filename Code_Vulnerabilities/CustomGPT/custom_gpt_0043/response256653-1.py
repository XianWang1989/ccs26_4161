
from PIL import Image

# Create a new image (RGB mode) and fill it with a color
img = Image.new('RGB', (100, 100), color='red')

# Save the image as a JPEG file
img.save('test_image.jpg')

# Now try opening the image
try:
    img_loaded = Image.open('test_image.jpg')
    img_loaded.show()  # This will open the image in the default viewer
    print("JPEG support is working!")
except Exception as e:
    print(f"Error opening JPEG: {e}")
