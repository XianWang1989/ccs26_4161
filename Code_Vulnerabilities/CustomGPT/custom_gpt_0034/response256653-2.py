
from PIL import Image

# Test JPEG loading
def test_jpeg_support(jpeg_file):
    try:
        img = Image.open(jpeg_file)
        img.show()
        print("JPEG file opened successfully.")
    except IOError:
        print("Failed to open JPEG file. JPEG support may not be available.")

# Replace 'test.jpg' with your actual JPEG file path
test_jpeg_support('test.jpg')
