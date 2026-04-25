
from PIL import Image

# Create an image in RGB mode
image = Image.new('RGB', (100, 100), color = 'red')

# Save as JPEG
image.save('test_image.jpg')

# Try to open the saved JPEG image
try:
    img = Image.open('test_image.jpg')
    img.show()  # This should display the image
    print("JPEG support is working!")
except Exception as e:
    print("Failed to open JPEG image:", e)
