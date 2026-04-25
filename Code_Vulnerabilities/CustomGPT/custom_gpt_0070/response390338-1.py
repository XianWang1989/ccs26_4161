
from PIL import Image
import numpy as np

def load_texture(file_path):
    image = Image.open(file_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # OpenGL expects the origin at the bottom-left
    return np.array(image)

image = load_texture('../imtools/image/ummagumma.jpg')
