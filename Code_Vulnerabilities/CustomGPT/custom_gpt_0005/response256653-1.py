
from PIL import Image

# Open a JPEG image file
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image
    # Perform some operations
    img = img.rotate(45)  # Rotate the image
    img.save("rotated_example.jpg")  # Save as a new JPEG file
except IOError:
    print("Unable to open or manipulate the JPEG image.")
