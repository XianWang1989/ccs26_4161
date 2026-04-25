
from PIL import Image

# Create a simple RGB image (just a solid color)
img = Image.new('RGB', (100, 100), color = 'blue')

# Save it as a JPEG file
img.save('test_image.jpg')

# Now try to open it again
img_opened = Image.open('test_image.jpg')
img_opened.show()  # This should open the image if JPEG support is working
