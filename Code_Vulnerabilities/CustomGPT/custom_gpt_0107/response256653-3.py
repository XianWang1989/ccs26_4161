
from PIL import Image

# Create a simple red image and save it as JPEG
red_image = Image.new('RGB', (100, 100), color='red')
red_image.save('test_image.jpg')

# Open the saved JPEG image
opened_image = Image.open('test_image.jpg')
opened_image.show()  # This should display the image
