
from PIL import Image

def load_image(file_path):
    with Image.open(file_path) as img:
        img = img.convert("RGB")
        return np.array(img)

# Usage
image = load_image('../imtools/image/ummagumma.jpg')
tx_id = tx2gpu(image)
