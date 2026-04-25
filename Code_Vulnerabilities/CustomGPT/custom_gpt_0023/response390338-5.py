
image = imread('../imtools/image/ummagumma.jpg')

# Flip image if needed
image = np.flipud(image)

# Ensure RGB format
if image.shape[2] == 4:  # RGBA
    image = image[:, :, :3]  # Discard the alpha channel

# Sending the image to the GPU
tx_id = tx2gpu(image)
