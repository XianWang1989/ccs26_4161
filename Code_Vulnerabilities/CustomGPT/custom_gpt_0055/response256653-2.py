
from PIL import Image

# Open an existing JPEG image
try:
    img = Image.open('test_image.jpg')
    img.show()  # Display the image

    # Perform some manipulation
    img = img.convert('L')  # Convert to grayscale
    img.save('test_image_gray.jpg')  # Save as a new JPEG
except IOError as e:
    print(f"Error: {e}")
