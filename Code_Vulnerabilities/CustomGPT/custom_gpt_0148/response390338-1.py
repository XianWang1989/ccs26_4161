
import numpy as np
import glfw
import OpenGL.GL as gl
from imio import imread, swap_rb

def setup_texture(image):
    if image.ndim == 3 and image.shape[2] == 3:
        # Optionally check if image is uint8 type
        image = image.astype(np.uint8)

        # Ensure image is flipped vertically for OpenGL
        image = np.flipud(image)

        texture_id = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        return texture_id

    raise ValueError("Image format not supported")

# Main function code remains largely the same
if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "OpenGL Textures", None, None)
    glfw.make_context_current(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = imread('path/to/your/image.jpg')
    swap_rb(image)  # Make sure this function is defined
    texture_id = setup_texture(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        square(1.0)  # Drawing your square with texture
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()
