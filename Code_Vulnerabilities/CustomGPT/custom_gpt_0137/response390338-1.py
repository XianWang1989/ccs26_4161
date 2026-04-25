
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

# Initialize GLFW
if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello")
    glfw.glfwMakeContextCurrent(win)
    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load the image
    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag:
        swap_rb(image)
    # Ensure you rotate or flip the image if necessary
    if image.ndim == 3 and image.shape[2] == 3:  # Checking if image has 3 channels
        image = np.flipud(image)  # This will flip the image vertically

    # Pass the image to the GPU
    tx_id = tx2gpu(image)

    # Main loop
    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Bind and draw the square with texture
        txrefer(tx_id)
        square(2)
        txrefer(0)

        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()


def swap_rb(mat):
    X = mat[:, :, 2].copy()  # Swap R and B channels
    mat[:, :, 2] = mat[:, :, 0]
    mat[:, :, 0] = X
    return mat


def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    if type(color) != type(None):
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        for vertex in color:
            gl.glColor3f(*vertex[:3])  # RGB color
            gl.glVertex3f(s * vertex[3], s * vertex[3], 0)  # s controlled by color(0, 1)
        gl.glEnd()
    else:
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
        gl.glEnd()


def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Upload the texture to GPU
    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
