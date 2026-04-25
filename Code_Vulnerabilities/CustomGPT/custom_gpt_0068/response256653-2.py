
from PIL import Image

# Open a JPEG image file
try:
    with Image.open("example.jpg") as img:
        img.show()  # Display the image
        img.save("output.png")  # Save it as a PNG
except IOError as e:
    print(f"Error opening or processing image: {e}")
