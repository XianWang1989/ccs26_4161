
from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100), color = 'red')

# Save the image as a JPEG
img.save('test_image.jpg')

# Check if the image was saved correctly
img_jpeg = Image.open('test_image.jpg')
img_jpeg.show()
