
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)  
    square(2)  
    txrefer(0)  
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()

# Cleanup
glfw.glfwDestroyWindow(win)
glfw.glfwTerminate()
