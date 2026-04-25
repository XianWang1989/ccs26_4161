
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Using OpenCV for image loading

def load_image(filename):
    image = cv2.imread(filename)
    if image is None:
        raise ValueError("Image not found or unable to load.")
    return image

def swap_rb(image):
    image = image[:, :, [2, 1, 0]]
    return image

def tx2gpu(image, flip=True):
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)

    # Ensure correct format: OpenGL expects channels in RGB order
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square():
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex2f(-0.5, -0.5)
    gl.glTexCoord2f(1, 0); gl.glVertex2f(0.5, -0.5)
    gl.glTexCoord2f(1, 1); gl.glVertex2f(0.5, 0.5)
    gl.glTexCoord2f(0, 1); gl.glVertex2f(-0.5, 0.5)
    gl.glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "Texture Example", None, None)
    glfw.make_context_current(window)

    # Clear color
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load and set texture
    image = load_image('path_to_image.jpg')
    image = swap_rb(image)
    texture_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Bind texture and draw square
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        square()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
