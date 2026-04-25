
from PIL import Image

# Create a new JPEG image
img = Image.new('RGB', (100, 100), color='blue')
img.save('blue_image.jpg')

# Open and manipulate the JPEG image
img_jpeg = Image.open('blue_image.jpg')
img_jpeg.show()
