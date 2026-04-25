
from PIL import Image

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Save the image as JPEG
img.save('test_image.jpg')

# Open the saved JPEG image
loaded_img = Image.open('test_image.jpg')
loaded_img.show()
