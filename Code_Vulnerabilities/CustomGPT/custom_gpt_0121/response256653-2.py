
from PIL import Image

# Create a simple image and save as JPEG
try:
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('test_image.jpg', 'JPEG')
    print("JPEG image created successfully.")

    # Open and show the created JPEG image
    img_opened = Image.open('test_image.jpg')
    img_opened.show()

except Exception as e:
    print("Error:", e)
