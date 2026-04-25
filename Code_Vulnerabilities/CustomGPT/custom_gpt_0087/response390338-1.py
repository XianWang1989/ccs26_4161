
def load_and_prepare_texture(image_path):
    # Load image using OpenCV
    image = imread(image_path)

    # Check for the correct shape
    if image.shape[2] != 3:
        raise ValueError("Image must have 3 color channels (RGB).")

    # Adjust for color format
    if rgb_flag:
        swap_rb(image)

    # Rotate image if necessary
    # Uncomment if you intend to rotate
    # image = np.rot90(image)

    # Send the image data to GPU
    return tx2gpu(image)

# Main loop adjustment
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    tx_id = load_and_prepare_texture('../imtools/image/ummagumma.jpg')  # Example image path
    txrefer(tx_id)
    square(2)
    txrefer(0)  
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
