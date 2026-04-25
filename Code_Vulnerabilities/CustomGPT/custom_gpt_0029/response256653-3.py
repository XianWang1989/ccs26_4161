
from PIL import Image

# Open an existing JPEG image
image_path = "example.jpg"
try:
    img = Image.open(image_path)
    img = img.convert("RGB")  # Convert to RGB if necessary
    img.show()  # Display the image
    img.save("output.jpg")  # Save the image as JPEG
    print("Image processed successfully.")
except Exception as e:
    print("Error:", e)
