
from PIL import Image

# Open a JPEG image
try:
    img = Image.open('example.jpg')  # Make sure to have a valid JPEG file in the same directory
    img.show()  # This should open the image using the default image viewer
except IOError:
    print("Unable to open JPEG file. Ensure Pillow supports JPEG and the file exists.")

# Save a PNG as JPEG (if above works successfully)
img = img.convert('RGB')  # Convert if necessary
img.save('output_image.jpg', 'JPEG')
print("Saved image as JPEG.")
