
from PIL import Image

try:
    # Create an example image
    image = Image.new('RGB', (100, 100), color='red')
    image.save('test_image.jpg')  # Save as JPEG

    # Open and display the JPEG image
    img = Image.open('test_image.jpg')
    img.show()
except Exception as e:
    print(f"An error occurred: {e}")
