
from PIL import Image

# Attempt to open a JPEG file
try:
    img = Image.open('example.jpg')  # Replace 'example.jpg' with your JPEG file path
    img.show()  # This should display the image
except IOError as e:
    print(f"An error occurred: {e}")

# Optionally, save the image in a different format
img.save('output.png', 'PNG')  # Converts and saves the JPEG to PNG
