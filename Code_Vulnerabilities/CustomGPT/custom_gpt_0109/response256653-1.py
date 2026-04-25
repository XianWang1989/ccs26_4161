
from PIL import Image

# Create a new JPEG image
try:
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('test_image.jpg', 'JPEG')
    print("JPEG image created successfully.")

    # Open and display the JPEG image
    img_opened = Image.open('test_image.jpg')
    img_opened.show()
except Exception as e:
    print(f"An error occurred: {e}")
