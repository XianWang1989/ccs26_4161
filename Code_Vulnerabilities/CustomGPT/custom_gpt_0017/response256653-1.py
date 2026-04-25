
from PIL import Image

# Open a JPEG image
img = Image.open('example.jpg')

# Perform some operations
img = img.rotate(90)  # Rotate image by 90 degrees
img.show()  # Display the image
img.save('example_rotated.jpg')  # Save the modified image
