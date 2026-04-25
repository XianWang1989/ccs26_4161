
from PIL import Image

# Create a sample JPEG image
img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg')

# Open the created JPEG image
img2 = Image.open('test_image.jpg')
img2.show()
