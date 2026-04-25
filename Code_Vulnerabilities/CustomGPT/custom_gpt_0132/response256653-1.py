
from PIL import Image

# Check JPEG support
try:
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('test.jpg')
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
