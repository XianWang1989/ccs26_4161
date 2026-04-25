
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag: 
    swap_rb(image)
tx_id = tx2gpu(image)  # Sending image to GPU for texturing

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)  
    square(2)  # Draw square with texture
    txrefer(0)  
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
