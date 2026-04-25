
image = imread('path/to/image.jpg')
image = np.rot90(image, k=1)  # Rotate 90 degrees clockwise
if not rgb_flag:
    image = swap_rb(image)  # Color component swap
