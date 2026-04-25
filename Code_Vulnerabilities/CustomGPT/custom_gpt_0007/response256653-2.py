
from PIL import Image

print("Pillow Version:", Image.__version__)
print("JPEG Support:", Image.core.plugins["jpeg"].__module__)
