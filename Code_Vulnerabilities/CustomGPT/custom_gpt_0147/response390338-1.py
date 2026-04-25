
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb

def check_image(image):
    # Ensure the image is a 3-channel RGB image
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Image must be a 3-channel RGB image")
    return image

def load_and_prepare_texture(file_path):
    image = imread(file_path)
    if not rgb_flag: 
        image = swap_rb(image)

    image = check_image(image)  # Check image validity
    tx_id = tx2gpu(image)
    return tx_id

# Main window setup
if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "OpenGL Texturing", None, None)
    glfw.glfwMakeContextCurrent(win)
    glfw.glfwSwapInterval(1)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)
    image_path = '../imtools/image/ummagumma.jpg'

    tx_id = load_and_prepare_texture(image_path)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)

        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
