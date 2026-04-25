
if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl
    import numpy as np
    from cv2 import imread  # Ensure you are importing OpenCV correctly

    # ... (initializations and GLFW setup)

    image = imread('../imtools/image/ummagumma.jpg')
    if image is None:
        print("Could not load image!")
        sys.exit(1)

    if image.ndim == 3 and image.shape[2] == 4:
        image = image[:, :, :3]  # Remove alpha channel if present

    if rgb_flag: 
        swap_rb(image)

    image = np.rot90(image)  # Rotate the image if needed
    tx_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id); square(2); txrefer(0)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    # Cleanup
    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
