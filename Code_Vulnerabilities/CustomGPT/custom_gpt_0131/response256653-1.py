
from PIL import Image

# Try to open a JPEG image
try:
    img = Image.open("example.jpg")  # Replace with your JPEG file
    img.show()  # This will open the image using the default image viewer
    print("JPEG image opened successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
