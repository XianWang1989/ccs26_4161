
import cv2

def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Ensure it's loaded in color
    if image is None:
        raise ValueError("Could not load image.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
