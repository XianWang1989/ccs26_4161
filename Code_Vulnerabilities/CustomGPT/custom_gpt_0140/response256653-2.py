
from PIL import Image

# Open a JPEG image
img = Image.open("example.jpg")
img.show()  # Display the image

# Save it as a PNG
img.save("output.png")
