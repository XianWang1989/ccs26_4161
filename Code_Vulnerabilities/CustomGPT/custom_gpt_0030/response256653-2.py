
from PIL import Image

# Create a simple red square and save it as JPEG
red_square = Image.new("RGB", (100, 100), "red")
red_square.save("red_square.jpg")

# Try opening the saved JPEG
try:
    img = Image.open("red_square.jpg")
    img.show()  # Should display the image if JPEG support is working
    print("JPEG opened successfully.")
except Exception as e:
    print("Failed to open JPEG:", e)
