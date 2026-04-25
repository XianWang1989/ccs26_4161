
# Inside your main function
tx_id = load_texture('../imtools/image/ummagumma.jpg')
if tx_id is None:  # Handle the error if the texture couldn't be loaded
    sys.exit("Failed to load texture.")

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)  
    square(2)  
    txrefer(0)  
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
