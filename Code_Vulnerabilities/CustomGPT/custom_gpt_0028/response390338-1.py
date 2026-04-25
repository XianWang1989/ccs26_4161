
def load_and_send_texture(image_path):
    image = imread(image_path)
    if rgb_flag:  # Assuming rgb_flag tells whether to swap channels
        swap_rb(image)

    # Flip the image vertically
    image = np.flipud(image)

    # Send the image to the GPU
    return tx2gpu(image)

# In your main loop
image_path = '../imtools/image/ummagumma.jpg'
tx_id = load_and_send_texture(image_path)
