
from PIL import Image

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'red')

# Save as JPEG
try:
    image.save('test_image.jpg')
    print("JPEG image saved successfully!")
except Exception as e:
    print(f"Failed to save JPEG image: {e}")

# Try opening the saved JPEG
try:
    img = Image.open('test_image.jpg')
    img.show()
except Exception as e:
    print(f"Failed to open JPEG image: {e}")
