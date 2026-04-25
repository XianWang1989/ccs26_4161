
from PIL import Image

# Create a simple JPEG image
try:
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg')
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
