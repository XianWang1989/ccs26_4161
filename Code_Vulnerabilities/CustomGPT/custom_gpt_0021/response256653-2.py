
from PIL import Image

# Open an existing JPEG image
try:
    image = Image.open("path_to_your_image.jpg")
    # Perform some operations, e.g., convert to grayscale
    gray_image = image.convert("L")

    # Save the new image
    gray_image.save("converted_image.jpg")

    print("Image processed and saved successfully.")
except IOError:
    print("Unable to open or process the image.")
