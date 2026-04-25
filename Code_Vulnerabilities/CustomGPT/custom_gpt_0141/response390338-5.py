
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2

from square import square
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

def main():
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)

    image = cv2.imread('../imtools/image/ummagumma.jpg')
    if image is None:
        print("Error: Could not read image.")
        return

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    # Optionally rotate and adjust the image if needed
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

if __name__ == '__main__':
    main()
