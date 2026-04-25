
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from square import square
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)
    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load and process the image
    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag: 
        swap_rb(image)

    # To avoid distortion, consider resizing if not power of two
    if not (image.shape[0] & (image.shape[0] - 1) == 0) and \
           not (image.shape[1] & (image.shape[1] - 1) == 0):
        # Resize the image if necessary (e.g., using OpenCV)
        import cv2
        image = cv2.resize(image, (256, 256))  # Choose appropriate dimensions

    # Optional: Rotating the image (ensure dimensions are swapped)
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
