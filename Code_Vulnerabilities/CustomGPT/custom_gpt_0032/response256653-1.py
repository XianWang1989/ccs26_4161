
from PIL import Image

# Create a simple RGB image
img = Image.new('RGB', (100, 100), color='blue')
img.save('test_image.jpg')

# Try opening the saved image
try:
    img_jpeg = Image.open('test_image.jpg')
    img_jpeg.show()
    print("JPEG support is working!")
except IOError:
    print("JPEG support is not working.")
