
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Use cv2 for loading images

def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to load")

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Rotate if necessary (example: rotate 90 degrees)
    # image = np.rot90(image)

    # Flip the image vertically
    image = np.flipud(image)

    # Get dimensions
    yres, xres, _ = image.shape

    # Create texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Upload texture to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    return texture_id

def render_square(texture_id):
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0.0, 0.0); gl.glVertex2f(-0.5, -0.5)
    gl.glTexCoord2f(0.0, 1.0); gl.glVertex2f(-0.5, 0.5)
    gl.glTexCoord2f(1.0, 1.0); gl.glVertex2f(0.5, 0.5)
    gl.glTexCoord2f(1.0, 0.0); gl.glVertex2f(0.5, -0.5)
    gl.glEnd()

if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "Texture Example", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('../imtools/image/ummagumma.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glEnable(gl.GL_TEXTURE_2D)

        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        render_square(texture_id)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
