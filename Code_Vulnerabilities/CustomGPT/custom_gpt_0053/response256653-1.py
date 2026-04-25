
from PIL import Image

# Create an image
img = Image.new('RGB', (100, 100), color = 'red')

# Save as JPEG
img.save('test_image.jpg')

# Open the image back
img_loaded = Image.open('test_image.jpg')
img_loaded.show()
