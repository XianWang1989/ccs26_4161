from PIL import Image

try:
    img = Image.open("test.jpg")  # Replace with an actual JPEG file path
    img.load()
    print("JPEG support is working.")
except IOError as e:
    print("JPEG support is not working:", e)
