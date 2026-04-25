
from PIL import Image

# Open a JPEG image
try:
    img = Image.open('example.jpg')  # Replace with your JPEG file path
    print("Image format:", img.format)
    print("Image size:", img.size)

    # Perform a simple operation: Convert to PNG and save
    img.save('output.png', 'PNG')
    print("Conversion successful, saved as output.png.")
except IOError as e:
    print("An error occurred:", e)
