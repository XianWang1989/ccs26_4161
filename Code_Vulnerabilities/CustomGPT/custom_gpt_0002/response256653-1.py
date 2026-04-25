
from PIL import Image

# Create a new image and save as JPEG
image = Image.new('RGB', (100, 100), color = 'red')
image.save('test_image.jpg')

# Open and display the image
image_opened = Image.open('test_image.jpg')
image_opened.show()
