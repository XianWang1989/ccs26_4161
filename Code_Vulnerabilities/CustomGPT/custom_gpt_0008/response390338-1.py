
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from square import square
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

def load_texture(file_path):
    # Load image using OpenCV
    image = imread(file_path)
    if not rgb_flag: 
        swap_rb(image)

    # Optional: Comment this out if flipping is causing issues
    # image = np.flipud(image)

    return tx2gpu(image)

if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "OpenGL Texture Example")
    glfw.glfwMakeContextCurrent(win)

    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load texture
    tx_id = load_texture('../imtools/image/ummagumma.jpg')

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
