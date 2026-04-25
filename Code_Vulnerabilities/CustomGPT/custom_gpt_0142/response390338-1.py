
import OpenGL.GL as gl
import numpy as np
from numpy import flipud

def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Use .astype(np.uint8) to ensure the data type is correct
    if len(image.shape) == 3 and image.shape[2] == 3:  # Check if image is RGB
        yres, xres, cresc = image.shape
        # OpenGL expects the image to be bottom-up
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, flipud(image.astype(np.uint8)))
    else:
        print("Error: Input image must be in RGB format.")

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
