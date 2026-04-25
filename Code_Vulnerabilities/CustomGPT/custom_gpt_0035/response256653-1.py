
from PIL import Image

# Open an existing JPEG image
image = Image.open('example.jpg')

# Perform an operation (e.g., convert to PNG)
image.save('converted.png', 'PNG')
