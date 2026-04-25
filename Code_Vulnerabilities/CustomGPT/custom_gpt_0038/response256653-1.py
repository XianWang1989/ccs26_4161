
from PIL import Image

# Open a JPEG image
try:
    img = Image.open('example.jpg')
    img.show()

    # Perform some manipulation: rotating the image
    rotated_img = img.rotate(90)
    rotated_img.save('rotated_example.jpg')
    print("Image rotation complete and saved as 'rotated_example.jpg'.")

except IOError:
    print("Unable to open or manipulate the image.")
