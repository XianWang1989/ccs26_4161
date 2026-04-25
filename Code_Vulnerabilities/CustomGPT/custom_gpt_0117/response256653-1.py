
from PIL import Image

try:
    # Create a new image with RGB mode
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg', 'JPEG')
    print("JPEG support is working. Test image created.")
except Exception as e:
    print(f"An error occurred: {e}")
