
from PIL import Image

try:
    img = Image.open('example.jpg')  # Ensure you have an example.jpg to test
    img.save('output.png')
    print("JPEG support is working!")
except Exception as e:
    print("Error:", e)
