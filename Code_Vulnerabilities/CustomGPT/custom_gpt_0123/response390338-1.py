
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Ensure you use OpenCV for image loading

def swap_rb(mat):
    """ Swap red and blue channels in the image """
    mat[..., 0], mat[..., 2] = mat[..., 2], mat[..., 0]
    return mat

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Flip the image vertically if using OpenCV
    if flip:
        image = np.flipud(image)

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

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

def main():
    if not glfw.init():
        return

    win = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(win)

    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Load your image
        image = cv2.imread('../imtools/image/ummagumma.jpg')
        swap_rb(image)  # Ensure color channels are correct
        tx_id = tx2gpu(image)  # Send to GPU

        txrefer(tx_id)
        square(2)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.destroy_window(win)
    glfw.terminate()

if __name__ == "__main__":
    main()
