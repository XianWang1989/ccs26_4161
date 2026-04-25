
from PIL import Image

# Open an existing JPEG image
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image

    # Perform some operations (e.g., convert to PNG)
    img.save("converted_image.png")
    print("Image converted and saved as 'converted_image.png'")
except IOError as e:
    print("An error occurred:", e)
