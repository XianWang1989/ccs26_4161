
from PIL import Image

# Create a new image using RGB mode
img = Image.new('RGB', (100, 100), color='red')

# Save the image as a JPEG file
img.save('test_image.jpg')

# Try opening the JPEG file
loaded_img = Image.open('test_image.jpg')
loaded_img.show()
