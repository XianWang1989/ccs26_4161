
from PIL import Image

try:
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.jpg')
    img_loaded = Image.open('test_image.jpg')
    img_loaded.show()
    print("JPEG support is working!")
except Exception as e:
    print("JPEG support is not working:", e)
