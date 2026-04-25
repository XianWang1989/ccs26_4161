
from PIL import Image

def test_jpeg_support(image_path):
    try:
        img = Image.open(image_path)
        img.load()  # Load the image to ensure JPEG support is working
        print("JPEG support is available!")
        img.show()  # Display the image
    except Exception as e:
        print(f"JPEG support is NOT available: {e}")

# Here, provide a path to your test JPEG image.
test_jpeg_support("path/to/your/test.jpg")
