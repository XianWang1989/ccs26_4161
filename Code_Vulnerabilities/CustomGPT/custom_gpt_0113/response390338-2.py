
if __name__ == '__main__':
    # Initialization code...

    image_path = '../imtools/image/ummagumma.jpg'
    image = load_and_prepare_texture(image_path)
    tx_id = tx2gpu(image)

    # Main loop...
