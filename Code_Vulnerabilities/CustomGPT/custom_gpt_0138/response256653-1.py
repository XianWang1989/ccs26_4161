
from PIL import Image

try:
    # Create a simple image and save it as JPEG
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('test.jpg')
    print("JPEG image created successfully.")
except Exception as e:
    print(f"Error: {e}")
