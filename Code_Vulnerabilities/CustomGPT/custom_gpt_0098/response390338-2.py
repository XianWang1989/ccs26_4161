
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag:
    image = swap_rb(image)

tx_id = tx2gpu(image)  # Upload the texture to GPU
