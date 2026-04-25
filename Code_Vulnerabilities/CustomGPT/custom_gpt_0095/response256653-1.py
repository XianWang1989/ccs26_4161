
from PIL import Image

# Create a new RGB image
img = Image.new('RGB', (100, 100), color='red')

# Save the image as JPEG
img.save('test_image.jpg')

# Open the image back to verify
img_loaded = Image.open('test_image.jpg')
img_loaded.show()
