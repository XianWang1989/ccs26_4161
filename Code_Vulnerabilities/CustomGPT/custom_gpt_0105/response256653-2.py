
from PIL import Image

# Open a JPEG image file
try:
    img = Image.open('test.jpg')  # replace 'test.jpg' with your image path
    img.show()  # This should display the image if JPEG support is working
except Exception as e:
    print(f"Error opening image: {e}")
