
import OpenGL.GL as gl
import numpy as np
from numpy import flipud

def tx2gpu(image, flip=True, unit=0):
    if image.ndim != 3 or image.shape[2] not in [3, 4]:
        raise ValueError("Image must be a 3-channel (RGB) or 4-channel (RGBA) array.")

    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Flip the image vertically
    if flip:
        image = flipud(image)

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
