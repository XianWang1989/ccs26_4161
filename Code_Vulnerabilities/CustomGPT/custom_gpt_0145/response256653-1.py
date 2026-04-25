
from PIL import Image

# Create a new image using RGB mode
img = Image.new('RGB', (100, 100), color = (155, 0, 0))

# Save the image in JPEG format
img.save('test_image.jpg')

# Check if the file has been created successfully
try:
    img = Image.open('test_image.jpg')
    img.show()
    print("JPEG support is working!")
except Exception as e:
    print("JPEG support is not working:", e)
