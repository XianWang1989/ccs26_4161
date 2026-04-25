
from PIL import Image

# Open a JPEG image
try:
    img = Image.open('example.jpg')  # Replace with your JPEG file
    img.show()  # Display the image
    img.save('output.png')  # Save as PNG
    print("JPEG support is working!")
except IOError:
    print("JPEG support is NOT working!")
