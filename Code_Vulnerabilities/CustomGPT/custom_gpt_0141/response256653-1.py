
from PIL import Image

# Open an existing JPEG file
image_path = 'example.jpg'
try:
    img = Image.open(image_path)
    print(f"Image format: {img.format}, Size: {img.size}, Mode: {img.mode}")

    # Perform some basic image manipulation
    img = img.rotate(90)  # Rotate the image by 90 degrees

    # Save the manipulated image as a new JPEG file
    img.save('rotated_example.jpg')
    print("Image saved as 'rotated_example.jpg'.")
except IOError as e:
    print(f"An error occurred: {e}")
