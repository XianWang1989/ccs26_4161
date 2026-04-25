
from PIL import Image

try:
    # Create an example JPEG image
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg')

    # Open the saved JPEG image
    img_opened = Image.open('test_image.jpg')
    img_opened.show()

    print("JPEG support working!")
except Exception as e:
    print(f"Error: {e}")
