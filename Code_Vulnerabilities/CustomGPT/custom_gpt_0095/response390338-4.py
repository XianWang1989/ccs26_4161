
if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl
    import numpy as np
    from imio import imread, rgb_flag, swap_rb
    from txio import tx2gpu, txrefer

    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)

    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag:
        swap_rb(image)

    # Example rotation if needed
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
