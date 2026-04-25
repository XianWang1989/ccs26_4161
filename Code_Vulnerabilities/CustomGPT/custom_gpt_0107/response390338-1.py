
import glfw
import OpenGL.GL as gl
import numpy as np
from OpenCV import imread

def swap_rb(mat):
    """ Swap Red and Blue channels """
    mat[..., [0, 2]] = mat[..., [2, 0]]
    return mat

def tx2gpu(image, flip=True):
    """ Upload the image to the GPU as a texture. """
    gl.glActiveTexture(gl.GL_TEXTURE0)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Flip the image vertically
    if flip:
        image = np.flipud(image)

    # Send texture data to OpenGL
    height, width, channels = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square_with_texture(texture_id):
    """ Draw a square with texture applied. """
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-0.5, -0.5, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-0.5, 0.5, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(0.5, 0.5, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(0.5, -0.5, 0)
    gl.glEnd()
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

if __name__ == '__main__':
    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW can't be initialized")

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    # Load and prepare image
    image = imread('path/to/image.jpg')
    image = swap_rb(image)  # Swap Red and Blue channels
    texture_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        square_with_texture(texture_id)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
