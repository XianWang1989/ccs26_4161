
from PIL import Image

# Create a new red image
img = Image.new('RGB', (100, 100), color='red')

# Save as JPEG
img.save('red_image.jpg')

# Now load the saved image to check if it works
try:
    loaded_img = Image.open('red_image.jpg')
    loaded_img.show()  # This will open the image
except IOError:
    print("JPEG support is not available.")
