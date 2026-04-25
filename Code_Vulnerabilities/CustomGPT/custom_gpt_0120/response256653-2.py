
from PIL import Image

# Attempt to open a JPEG file
try:
    img = Image.open('test_image.jpg')  # Replace with your JPEG file path
    img.show()  # Displays the image
    img.save('output_image.jpg')  # Saves a copy of the image
    print("JPEG support is working!")
except Exception as e:
    print(f"Error: {e}")
