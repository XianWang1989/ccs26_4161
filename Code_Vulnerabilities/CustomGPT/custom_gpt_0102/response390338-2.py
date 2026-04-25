
from PIL import Image

def load_image(file_path):
    img = Image.open(file_path)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image
    img_array = np.array(img)
    return img_array
