
from PIL import Image

# Create a simple JPEG image
img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg')

# Try opening the generated image
try:
    img = Image.open('test_image.jpg')
    img.show()
except Exception as e:
    print(f"Error: {e}")
