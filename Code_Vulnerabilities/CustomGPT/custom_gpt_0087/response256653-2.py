
from PIL import Image

# Replace 'sample.jpg' with your actual JPEG file name
try:
    image = Image.open('sample.jpg')
    image.load()  # Load the image
    print("JPEG image successfully loaded.")
except Exception as e:
    print(f"Error loading JPEG image: {e}")
