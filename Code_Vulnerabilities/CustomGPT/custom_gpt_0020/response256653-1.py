
from PIL import Image

# Try to open a JPEG file
try:
    img = Image.open("test.jpg")
    img.show()  # This should display the image if it works
    img.save("test_copy.jpg")  # This tries to save as a JPEG
    print("JPEG processing works!")
except Exception as e:
    print("Error processing JPEG:", e)
