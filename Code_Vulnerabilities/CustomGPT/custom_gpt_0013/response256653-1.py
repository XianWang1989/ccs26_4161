
from PIL import Image

try:
    # Create a new image and save it as JPEG
    image = Image.new('RGB', (100, 100), color = 'red')
    image.save('test_image.jpg')

    # Open the image to check if JPEG support is working
    img = Image.open('test_image.jpg')
    img.show()

    print("JPEG support is working!")
except Exception as e:
    print(f"An error occurred: {e}")
