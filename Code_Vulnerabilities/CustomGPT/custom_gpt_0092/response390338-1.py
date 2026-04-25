
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb

# Initialize GLFW and create a window
if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load and prepare image
    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag:
        image = swap_rb(image)

    # Perform a rotation if necessary
    # Uncomment if needed
    # image = np.rot90(image)

    tx_id = tx2gpu(image)

    # Main loop
    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()

# Square function with proper texture coordinates
def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

# Texture loading function with image flipping
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)  # Flipping image vertically

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
