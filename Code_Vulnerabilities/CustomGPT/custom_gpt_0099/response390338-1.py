
image = imread('../imtools/image/ummagumma.jpg')
if image.shape[2] == 4:  # Check for RGBA
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
