
from PIL import Image

# Create a simple image
img = Image.new('RGB', (100, 100), color='red')

# Save the image as a JPEG file
img.save('test_image.jpg')

# Open the image to confirm it's saved properly
img_loaded = Image.open('test_image.jpg')
print(img_loaded.format)  # Should output 'JPEG' if working correctly
