
from PIL import Image

# Test creating a JPEG image
img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg')

# Check if it can open a JPEG image
try:
    img2 = Image.open('test_image.jpg')
    img2.show()
    print("JPEG support is working!")
except Exception as e:
    print(f"Error opening JPEG: {e}")
