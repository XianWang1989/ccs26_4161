
from PIL import Image

try:
    # Open a JPEG image file
    with Image.open("example.jpg") as img:
        img.show()  # This will display the image
        print("JPEG image opened successfully!")
except Exception as e:
    print(f"Error: {e}")
