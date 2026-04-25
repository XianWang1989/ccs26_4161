
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from OpenCV import imread

def swap_rb(mat):
    mat[:,:,0], mat[:,:,2] = mat[:,:,2], mat[:,:,0].copy()
    return mat

def tx2gpu(image):
    image = swap_rb(image)
    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, np.flipud(image))
    return gl.glGenTextures(1)

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glEnd()

if __name__ == '__main__':
    if not glfw.init():
        sys.exit()
    window = glfw.create_window(800, 800, "OpenGL Texture", None, None)
    glfw.make_context_current(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = imread('path_to_your_image.jpg')
    tx_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tx_id)
        square()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
