
from PIL import Image

# Create a simple JPEG image
img = Image.new('RGB', (100, 100), color = 'red')
img.save('test_image.jpg')

# Now try to open the JPEG file
try:
    img_opened = Image.open('test_image.jpg')
    img_opened.show()
except Exception as e:
    print(f"Failed to open JPEG: {e}")
