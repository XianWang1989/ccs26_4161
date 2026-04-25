
from PIL import Image

def test_jpeg_support():
    try:
        # Attempt to open a JPEG image
        img = Image.open('test_image.jpg')
        img.show()  # This should display the image
        print('JPEG support is working!')
    except Exception as e:
        print(f'Error: {e}')
        print('JPEG support is not working!')

test_jpeg_support()
