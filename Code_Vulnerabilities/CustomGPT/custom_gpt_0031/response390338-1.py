
image = imread('../imtools/image/ummagumma.jpg')
image = np.flipud(image)  # Flip image vertically
if not rgb_flag:
    swap_rb(image)
