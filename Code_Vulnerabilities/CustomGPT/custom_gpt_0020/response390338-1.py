
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Using OpenCV for image loading

def swap_rb(mat):
    mat[..., 0], mat[..., 2] = mat[..., 2], mat[..., 0]
    return mat

def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path {image_path} not found.")

    image = swap_rb(image)  # Swap Red and Blue channels

    # Flip the image vertically
    image = np.flipud(image)

    # Texture generation
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Define texture data
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind the texture
    return texture_id

def draw_square():
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0.0, 0.0); gl.glVertex3f(-0.5, -0.5, 0.0)
    gl.glTexCoord2f(0.0, 1.0); gl.glVertex3f(-0.5,  0.5, 0.0)
    gl.glTexCoord2f(1.0, 1.0); gl.glVertex3f(0.5,  0.5, 0.0)
    gl.glTexCoord2f(1.0, 0.0); gl.glVertex3f(0.5, -0.5, 0.0)
    gl.glEnd()

if __name__ == '__main__':
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    gl.glEnable(gl.GL_TEXTURE_2D)

    texture_id = load_texture('path_to_your_image.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        draw_square()
        glfw.swap_buffers(window)
        glfw.poll_events()

    gl.glDeleteTextures(1, [texture_id])  # Clean up texture

    glfw.terminate()
