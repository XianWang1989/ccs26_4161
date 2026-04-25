
from PIL import Image

def check_jpeg_support():
    try:
        img = Image.open('path_to_your_image.jpg')  # Replace with a valid JPEG file path
        print("JPEG support is working!")
        img.show()
    except Exception as e:
        print(f"Error: {e}")

check_jpeg_support()
