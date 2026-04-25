
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Ensure texture wrapping and filtering are set correctly
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape

    if flip:
        image = np.flipud(image)

    # Ensure texture image is set correctly
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id


# Example usage:
if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl
    import numpy as np
    from imio import imread

    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Texture Test")
    glfw.glfwMakeContextCurrent(win)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        image = imread('path_to_your_image.jpg')
        tx_id = tx2gpu(image)  # Load texture to GPU
        txrefer(tx_id)          # Bind texture to render
        square(2)               # Draw square
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwTerminate()
