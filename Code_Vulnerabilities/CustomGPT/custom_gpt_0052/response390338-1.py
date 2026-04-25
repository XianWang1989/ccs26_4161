
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Make sure to install OpenCV: pip install opencv-python

def swap_rb(image):
    """ Swap Red and Blue channels. """
    image[..., [0, 2]] = image[..., [2, 0]]
    return image

def load_texture(image_path):
    """ Load and upload texture to GPU. """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid.")
    image = swap_rb(image)  # Swap RB channels

    # Flip the image vertically
    image = np.flipud(image)

    height, width, channels = image.shape
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture for safety
    return texture_id

def draw_square(scale=1.0):
    """ Draw a textured square. """
    s = scale * 0.5
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

def main(image_path):
    # Initialize GLFW
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "Textured Square", None, None)
    glfw.make_context_current(window)

    # Load texture
    texture_id = load_texture(image_path)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        draw_square(2)  # Draw square
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        gl.glDisable(gl.GL_TEXTURE_2D)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main('../imtools/image/ummagumma.jpg')
