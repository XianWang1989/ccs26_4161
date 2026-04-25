
from PIL import Image

# Create an example image
img = Image.new('RGB', (100, 100), color = 'red')
img.save('test_image.jpg')  # Save as JPEG

# Load the JPEG image
loaded_img = Image.open('test_image.jpg')
loaded_img.show()  # Display the image
