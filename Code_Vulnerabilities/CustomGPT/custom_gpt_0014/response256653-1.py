
from PIL import Image

# Create a simple JPEG image
img = Image.new('RGB', (100, 100), color = 'red')

# Save it as a JPEG file
img.save('test_image.jpg')

# Open and display the JPEG image
try:
    img = Image.open('test_image.jpg')
    img.show()
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not available.")
