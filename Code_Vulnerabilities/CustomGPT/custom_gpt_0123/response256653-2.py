
from PIL import Image

# Create a simple image and save it as JPEG
img = Image.new('RGB', (100, 100), color = 'red')
img.save('test_image.jpg', 'JPEG')

# Open the JPEG image and show it
try:
    img_jpeg = Image.open('test_image.jpg')
    img_jpeg.show()
    print("JPEG image opened successfully.")
except IOError:
    print("JPEG support is not available.")
