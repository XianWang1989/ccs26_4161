
from PIL import Image

# Create a new image
img = Image.new('RGB', (100, 100), color = 'red')
img.save('test_image.jpg')

# Open the same image
img = Image.open('test_image.jpg')
img.show()
