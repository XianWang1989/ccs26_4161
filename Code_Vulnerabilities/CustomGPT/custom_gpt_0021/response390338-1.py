
import numpy as np
import glfw
import OpenGL.GL as gl
from cv2 import imread

def load_texture(filename):
    image = imread(filename)
    # Check if image is loaded properly
    if image is None:
        raise Exception("Could not load image")

    # Swap Red and Blue channels
    image = swap_rb(image)
    # Flip the image vertically
    image = np.flipud(image)

    # Generate and bind the texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Define the texture
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    return texture_id

def swap_rb(mat):
    mat[..., 0], mat[..., 2] = mat[..., 2], mat[..., 0]
    return mat

# OpenGL initialization code
if __name__ == '__main__':
    if not glfw.init():
        raise Exception("GLFW can't be initialized")

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created")

    glfw.make_context_current(window)

    # Load your texture
    texture_id = load_texture('path_to_your_image.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Bind and render your texture here

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
