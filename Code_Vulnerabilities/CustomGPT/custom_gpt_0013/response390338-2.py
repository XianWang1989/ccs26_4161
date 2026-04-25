
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Update the texture before drawing
    txrefer(tx_id)
    square(2)  # Draw square with texture
    txrefer(0)  # Disable texture

    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
