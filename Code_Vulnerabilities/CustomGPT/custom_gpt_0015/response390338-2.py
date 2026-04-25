
import cv2

image = cv2.imread('../imtools/image/ummagumma.jpg')
if image is None:
    print("Error loading image.")
else:
    print(f"Loaded image with shape {image.shape}, dtype {image.dtype}")
    if not rgb_flag:
        swap_rb(image)

    tx_id = tx2gpu(image)
