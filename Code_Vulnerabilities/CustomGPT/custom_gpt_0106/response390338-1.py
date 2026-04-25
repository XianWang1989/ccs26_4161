
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Ensure you have OpenCV installed

def swap_rb(mat):
    """ Swap the red and blue channels of an image. """
    mat = mat[..., [2, 1, 0]]  # swap channels
    return mat

def tx2gpu(image, flip=True, unit=0):
    """ Send the texture to the GPU. """
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)

    # Get dimensions and send texture data
    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square(texture_id):
    """ Draw a textured square. """
    size = 1.0
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-size, -size, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-size, size, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(size, size, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(size, -size, 0)
    gl.glEnd()
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

# GLFW and OpenGL initialization
if __name__ == '__main__':
    glfw.glfwInit()
    window = glfw.glfwCreateWindow(800, 800, "OpenGL Texture Example", None, None)
    glfw.glfwMakeContextCurrent(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load image using OpenCV
    image = cv2.imread('path_to_your_image.jpg')
    if image is not None:
        image = swap_rb(image)  # Swap channels
        texture_id = tx2gpu(image)

        while not glfw.glfwWindowShouldClose(window):
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            square(texture_id)  # Draw the square with texture
            glfw.glfwSwapBuffers(window)
            glfw.glfwPollEvents()
    else:
        print("Failed to load image.")

    glfw.glfwDestroyWindow(window)
    glfw.glfwTerminate()
