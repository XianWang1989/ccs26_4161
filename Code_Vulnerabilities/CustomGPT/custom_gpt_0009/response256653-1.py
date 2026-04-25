
from PIL import Image

try:
    # Open an existing JPEG file
    img = Image.open("example.jpg")
    img.show()  # Display the image
    img.save("example_copy.jpg")  # Save a copy
    print("JPEG processing is working!")
except IOError:
    print("JPEG processing failed.")
