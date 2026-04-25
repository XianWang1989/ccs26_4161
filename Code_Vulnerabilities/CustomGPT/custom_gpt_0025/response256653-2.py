
from PIL import Image

def test_jpeg_support(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        # Display the image
        img.show()
        print("JPEG support is working.")
    except IOError:
        print("JPEG support is not available. Please check your Pillow installation.")

# Replace 'sample.jpg' with the path to a valid JPEG image on your machine
test_jpeg_support('sample.jpg')
