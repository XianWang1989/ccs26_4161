
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Make sure to use OpenCV for img processing

def load_image(file_path):
    # Load image using OpenCV and swap channels
    image = cv2.imread(file_path)
    if image is None:
        raise Exception("Could not load image.")

    # Convert from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optionally flip the image if needed
    return np.flipud(image)

def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "OpenGL Texture Example", None, None)
    glfw.glfwMakeContextCurrent(win)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load and send texture to GPU
    image = load_image('../imtools/image/ummagumma.jpg')
    tx_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)  
        square(2)  # Adjust square() to use correct texture coordinates
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()
