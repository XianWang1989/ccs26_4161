
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, swap_rb  # Ensure these functions are correctly defined in your context

def tx2gpu(image):
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Upload texture to GPU
    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, np.flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

if __name__ == '__main__':
    # GLFW initialization omitted for brevity
    image = imread('path/to/image.jpg')
    swap_rb(image)  # Ensure this function swaps RGB correctly
    texture_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        square()
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    # Cleanup
    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
