
from PIL import Image

# Create a simple image
img = Image.new('RGB', (100, 100), color = (255, 0, 0))

# Save the image as a JPEG file
img.save('test_image.jpg')

# Load the JPEG file
loaded_img = Image.open('test_image.jpg')
loaded_img.show()
