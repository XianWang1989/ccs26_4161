
from PIL import Image

def test_jpeg_support():
    try:
        # Attempt to open a JPEG image
        img = Image.open("test.jpg")  # Replace with your image path
        img.load()  # Load the image
        print("JPEG support is functional.")
    except Exception as e:
        print(f"Error: {e}")

test_jpeg_support()
