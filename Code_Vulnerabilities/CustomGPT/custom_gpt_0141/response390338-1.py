
import cv2  # Make sure you use this for image reading
import numpy as np

# Ensure you read the image and convert it to RGB
image = cv2.imread('../imtools/image/ummagumma.jpg')
if image is None:
    print("Error: Could not read image.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
