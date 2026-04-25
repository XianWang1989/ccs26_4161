
def rotate_texture(image):
    return np.rot90(image)

# Usage
image = load_and_prepare_image(image_path)
rotated_image = rotate_texture(image)
tx_id = tx2gpu(rotated_image)
