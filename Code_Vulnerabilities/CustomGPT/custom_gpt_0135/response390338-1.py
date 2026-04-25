
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Using OpenCV for image loading

def swap_rb(image):
    """ Swap Red and Blue channels. """
    return image[..., [2, 1, 0]]  # Rearranging RGB to BGR

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)  # Flip image vertically

    # Upload the image to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

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

if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load and process image
    image = cv2.imread("path/to/your/image.jpg")  # Ensure correct path
    if image is not None:
        image = swap_rb(image)  # Swap RB channels
        # Optionally rotate image
        # image = np.rot90(image)

        tx_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # Bind texture and draw the square
        if image is not None:
            gl.glBindTexture(gl.GL_TEXTURE_2D, tx_id)
            square(2.0)
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
