
from PIL import Image

# Create a simple JPEG image
def create_jpeg_image():
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg')

# Try to open the JPEG image
def open_jpeg_image():
    try:
        img = Image.open('test_image.jpg')
        img.show()
    except Exception as e:
        print(f"Error opening JPEG: {e}")

create_jpeg_image()
open_jpeg_image()
