
from PIL import Image

# Attempt to open a JPEG image
try:
    img = Image.open('path/to/your/image.jpg')
    img.show()
    print("JPEG image opened successfully!")
except Exception as e:
    print("Error opening JPEG image:", e)
