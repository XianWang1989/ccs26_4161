
from PIL import Image

# Create a simple image and save it as a JPEG
image = Image.new('RGB', (100, 100), color = 'red')
image.save('test_image.jpg')

# Try to open the newly created JPEG image
try:
    img = Image.open('test_image.jpg')
    img.show()  # This should open the JPEG image if support is working
    print("JPEG support is functioning correctly!")
except Exception as e:
    print("Error:", e)
