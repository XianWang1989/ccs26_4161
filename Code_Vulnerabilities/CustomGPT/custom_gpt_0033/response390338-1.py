
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Use OpenCV for image loading

def swap_rb(image):
    image[..., [0, 2]] = image[..., [2, 0]]  # Swap R and B channels
    return image

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

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

def main():
    glfw.glfwInit()
    window = glfw.glfwCreateWindow(800, 800, "Hello", None, None)
    glfw.glfwMakeContextCurrent(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load the image
    image = cv2.imread('ummagumma.jpg')
    if image is None:
        print("Error loading image!")
        sys.exit()

    image = swap_rb(image)
    tx_id = tx2gpu(image)

    while not glfw.glfwWindowShouldClose(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tx_id)
        square()
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        glfw.glfwSwapBuffers(window)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(window)
    glfw.glfwTerminate()

if __name__ == '__main__':
    main()
