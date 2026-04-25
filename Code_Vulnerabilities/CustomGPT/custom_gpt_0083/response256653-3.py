
from PIL import Image

try:
    # Open a JPEG file
    img = Image.open('example.jpg')
    img.show()  # Display the image

    # Perform some manipulation
    img = img.rotate(90)  # Rotate the image by 90 degrees
    img.save('rotated_example.jpg')  # Save the rotated image
except IOError:
    print("Error: Unable to open or manipulate the image.")
