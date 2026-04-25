
from PIL import Image

# Create a simple example image and save it as JPEG
try:
    # Create a new image with RGB mode
    img = Image.new('RGB', (100, 100), color = 'red')

    # Save the image as a JPEG
    img.save('test_image.jpg')

    # Open the newly saved JPEG image
    img_jpeg = Image.open('test_image.jpg')
    img_jpeg.show()

    print("JPEG support is working!")
except Exception as e:
    print(f"An error occurred: {e}")
