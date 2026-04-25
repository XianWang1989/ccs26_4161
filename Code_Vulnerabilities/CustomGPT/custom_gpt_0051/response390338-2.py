
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag:
    image = swap_rb(image)
image = np.rot90(image)  # Apply rotation if needed
tx_id = tx2gpu(image)
