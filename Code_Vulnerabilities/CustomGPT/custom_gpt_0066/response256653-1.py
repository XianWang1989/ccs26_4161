
from PIL import Image

# Create a new JPEG image
img = Image.new('RGB', (100, 100), color = 'red')
img.save('test_image.jpg')

# Open the JPEG image
img_opened = Image.open('test_image.jpg')
img_opened.show()
