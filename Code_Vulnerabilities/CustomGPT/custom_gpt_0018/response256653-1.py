
from PIL import Image

# Open a JPEG image
try:
    img = Image.open('example.jpg')
    img.show()  # Display the image

    # Perform some manipulation (convert to grayscale)
    gray_img = img.convert('L')
    gray_img.save('example_gray.jpg')  # Save the manipulated image
    print("Successfully opened and manipulated JPEG image.")
except IOError:
    print("Error: Couldn't open or manipulate the image.")
