
if __name__ == '__main__':
    ...  # Initialization code

    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag: 
        image = swap_rb(image)

    # Uncomment this line to test rotation
    # image = np.rot90(image)

    tx_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
