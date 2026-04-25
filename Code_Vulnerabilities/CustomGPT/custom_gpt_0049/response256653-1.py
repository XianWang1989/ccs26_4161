
from PIL import Image

# Path to a JPEG image (make sure an image exists here)
jpeg_image_path = 'test_image.jpg'

try:
    # Open the JPEG image
    img = Image.open(jpeg_image_path)
    print(f'The image format is: {img.format}')

    # Perform a simple operation, like saving it as a PNG
    img.save('output_image.png')
    print('JPEG image processed and saved as PNG successfully!')
except IOError:
    print('Cannot open or process the JPEG image. Please check if Pillow has JPEG support.')
