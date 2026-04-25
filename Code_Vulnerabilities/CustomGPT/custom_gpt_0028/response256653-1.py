
from PIL import Image

try:
    # Open a JPEG image file
    img = Image.open('test.jpg')  # Replace 'test.jpg' with your JPEG file path
    img.show()  # This should open the image with the default image viewer

    # Perform some operation (e.g., converting to PNG)
    img.convert('RGB').save('output.png', 'PNG')
    print("JPEG loaded and converted successfully!")
except Exception as e:
    print(f"Error: {e}")
