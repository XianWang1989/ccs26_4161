
from PIL import Image

# Open a JPEG image
try:
    img = Image.open("example.jpg")
    img.show()
    img.save("output.png")  # Convert to PNG
except IOError:
    print("Unable to open or manipulate the JPEG file.")
