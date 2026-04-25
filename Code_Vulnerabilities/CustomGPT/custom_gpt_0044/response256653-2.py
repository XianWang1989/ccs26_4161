
from PIL import Image

# Open an existing JPEG image
try:
    img = Image.open('example.jpg')  # Replace with your image path
    img.show()  # Display the image

    # Perform some manipulation (e.g., rotate)
    img_rotated = img.rotate(90)
    img_rotated.save('rotated_example.jpg')  # Save the rotated image
    print("JPEG operations worked successfully!")
except IOError as e:
    print(f"An error occurred: {e}")
