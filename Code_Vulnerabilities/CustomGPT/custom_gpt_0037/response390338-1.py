
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Adjust texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape
    if flip:
        image = np.flipud(image)

    # Ensure that the image has 3 channels for RGB
    if image.shape[2] != 3:
        raise ValueError("Expected image with RGB channels")

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Load and prepare the image
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag: 
    swap_rb(image)
# Use rotation only if necessary
# image = np.rot90(image)  # Comment or uncomment based on your needs
tx_id = tx2gpu(image)
