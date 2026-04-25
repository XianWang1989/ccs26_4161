
from PIL import Image

# Create a new image
img = Image.new('RGB', (100, 100), color = 'red')

# Save as JPEG
img.save('test_image.jpg')

# Try opening the JPEG
try:
    loaded_img = Image.open('test_image.jpg')
    loaded_img.show()
    print("JPEG successfully created and opened!")
except Exception as e:
    print(f"Error: {e}")
