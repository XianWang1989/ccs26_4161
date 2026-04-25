
from PIL import Image

# Create a new JPEG image
try:
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg')
    print("JPEG image created and saved successfully.")

    # Open the created JPEG image
    img_loaded = Image.open('test_image.jpg')
    img_loaded.show()
    print("JPEG image loaded successfully.")
except Exception as e:
    print("Error:", e)
