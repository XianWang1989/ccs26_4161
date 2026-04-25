
def load_and_prepare_image(image_path):
    # Load image
    image = imread(image_path)

    # Check if image is loaded
    if image is None:
        raise ValueError("Image not found or cannot be loaded.")

    # Swap Red and Blue channels
    if rgb_flag: 
        swap_rb(image)

    # Handle image rotation if needed (you can also check EXIF data here)
    # Uncomment if necessary
    # image = np.rot90(image)

    return image

# In main function
if __name__ == '__main__':
    # ... (initialization code)

    # Load and prepare the image
    image_path = '../imtools/image/ummagumma.jpg'
    image = load_and_prepare_image(image_path)

    # Send to GPU
    tx_id = tx2gpu(image)
