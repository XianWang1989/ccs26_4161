
from PIL import Image

# Create a new image
image = Image.new('RGB', (100, 100), color='red')

# Save as JPEG
image.save('test_image.jpg')

# Open the JPEG file
img = Image.open('test_image.jpg')
img.show()
