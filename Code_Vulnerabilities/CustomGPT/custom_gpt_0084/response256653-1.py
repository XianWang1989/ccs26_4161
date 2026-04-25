
from PIL import Image

# Create a simple JPEG image
img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg')

# Try to open the JPEG image
try:
    img = Image.open('test_image.jpg')
    img.show()  # This should display the image
    print("JPEG processing works!")
except Exception as e:
    print(f"Error processing JPEG: {e}")
