
import cv2  # Ensure you have OpenCV installed

# Load image and ensure color channels are swapped
image = cv2.imread('../imtools/image/ummagumma.jpg')
if image is not None:
    # Swap Red and Blue channels
    swap_rb(image)  # Call your existing function
else:
    print("Failed to load image. Please check the file path.")

# Rotate image if necessary
# Uncomment the following line if you want to rotate the image
# image = np.rot90(image) 

# Handle texture generation:
tx_id = tx2gpu(image)
