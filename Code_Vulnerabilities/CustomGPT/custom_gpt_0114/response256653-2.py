
from PIL import Image

# Load a JPEG image
try:
    img = Image.open("example.jpg")
    img.show()  # Display the image
    img.save("output.png")  # Convert and save as PNG
    print("JPEG operations are working.")
except Exception as e:
    print(f"Error: {e}")
