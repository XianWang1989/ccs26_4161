
if image.shape[2] != 3:
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
