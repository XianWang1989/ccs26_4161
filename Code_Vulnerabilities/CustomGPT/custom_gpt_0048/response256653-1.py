
from PIL import Image

# Open a JPEG image
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image
except IOError:
    print("Unable to open the image.")

# Save the image as a PNG
img.save("example.png", format="PNG")
