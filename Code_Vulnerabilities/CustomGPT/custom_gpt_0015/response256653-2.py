
from PIL import Image

# Create a simple JPEG image
image = Image.new('RGB', (100, 100), color='red')
image.save('test_image.jpg', 'JPEG')

# Open the JPEG image
loaded_image = Image.open('test_image.jpg')
loaded_image.show()
