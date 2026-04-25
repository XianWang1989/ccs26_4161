
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from square import square
from imio import imread, rgb_flag, swap_rb

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Properly handle image dimensions
    yres, xres, cres = image.shape
    if flip:
        image = np.flipud(image)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main execution
if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)

    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load an image
    image = imread('../imtools/image/ummagumma.jpg')
    if rgb_flag:
        swap_rb(image)

    # Rotate if necessary
    image = np.rot90(image)

    # Upload texture to GPU
    tx_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
