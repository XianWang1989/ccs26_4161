
from PIL import Image

# Create a new image
image = Image.new('RGB', (100, 100), color='red')
image.save('test_image.jpg')  # Save as JPEG

# Open the image to verify
opened_image = Image.open('test_image.jpg')
opened_image.show()
