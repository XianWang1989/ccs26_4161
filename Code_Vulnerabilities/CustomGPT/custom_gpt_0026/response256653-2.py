
from PIL import Image

# Open a JPEG image file
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image

    # Perform basic operations
    img = img.rotate(90)  # Rotate the image
    img.save("rotated_example.jpg")  # Save the modified image
    print("Image processed successfully!")
except IOError:
    print("Failed to open or process the JPEG image.")
