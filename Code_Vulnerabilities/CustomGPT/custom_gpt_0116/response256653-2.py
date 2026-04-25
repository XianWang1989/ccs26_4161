
from PIL import Image

try:
    img = Image.open("test_image.jpg")  # Replace with your image path
    img.show()
    print("JPEG image loaded successfully.")
except Exception as e:
    print("Failed to load JPEG:", e)
