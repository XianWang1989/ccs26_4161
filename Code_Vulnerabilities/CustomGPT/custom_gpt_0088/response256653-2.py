
from PIL import Image

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'red')

# Save the image as a JPEG file
image.save('test_image.jpg')

# Try opening the saved JPEG
try:
    img = Image.open('test_image.jpg')
    img.show()
    print("JPEG image opened successfully!")
except IOError:
    print("Failed to open JPEG image.")
