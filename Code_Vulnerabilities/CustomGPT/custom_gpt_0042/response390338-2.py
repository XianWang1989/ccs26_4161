
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag:
    swap_rb(image)

# Rotate if necessary
# image = np.rot90(image)  # Uncomment if needed for specific images

# Handle texture upload
tx_id = tx2gpu(image)
