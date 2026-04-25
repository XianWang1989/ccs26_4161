
from PIL import Image

# Open a JPEG image
image_path = 'example.jpg'  # Path to your JPEG file
image = Image.open(image_path)

# Perform some operations (e.g., rotate and save)
rotated_image = image.rotate(45)
rotated_image.save('rotated_example.jpg')
print("Successfully manipulated the JPEG image.")
