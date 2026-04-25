
from PIL import Image

# Create an example image
img = Image.new('RGB', (100, 100), color='red')
img.save('example.jpg')  # Save as JPEG

# Now try to open the JPEG
img_loaded = Image.open('example.jpg')
img_loaded.show()  # This should open the JPEG in your default viewer
