
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Ensure you have OpenCV installed

def load_and_prepare_texture(filepath):
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Convert from BGR to RGB if using OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optionally resize to power-of-two dimensions (not shown here)

    # Flip the image vertically
    image = np.flipud(image)

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Upload the texture to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0],
                     0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture
    return texture_id

def display_texture(texture_id):
    gl.glEnable(gl.GL_TEXTURE_2D)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    # Draw your square or rectangle here
    # Remember to set texture coordinates
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex2f(-1, -1)
    gl.glTexCoord2f(1, 0); gl.glVertex2f(1, -1)
    gl.glTexCoord2f(1, 1); gl.glVertex2f(1, 1)
    gl.glTexCoord2f(0, 1); gl.glVertex2f(-1, 1)
    gl.glEnd()
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture
    gl.glDisable(gl.GL_TEXTURE_2D)

if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "OpenGL Texture", None, None)
    glfw.make_context_current(window)

    texture_id = load_and_prepare_texture('path_to_your_image.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        display_texture(texture_id)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
