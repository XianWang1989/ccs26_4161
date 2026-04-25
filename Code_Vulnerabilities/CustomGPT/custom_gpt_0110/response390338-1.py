
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Get dimensions and Make sure they are in the right format
    yres, xres, cres = image.shape
    if cres != 3:
        raise ValueError("Image must have 3 channels (RGB).")

    # Upload texture data
    if flip:
        image = np.flipud(image)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

if __name__ == '__main__':
    if not glfw.init():
        sys.exit()
    win = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(win)

    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag: swap_rb(image)
    tx_id = tx2gpu(image)

    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)
        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()
