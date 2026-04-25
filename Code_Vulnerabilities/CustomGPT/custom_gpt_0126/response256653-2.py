
from PIL import Image

# Attempt to open a JPEG image
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image
    img.save("output.png")  # Save as PNG to test writing
    print("JPEG support is working!")
except Exception as e:
    print("Error:", e)
