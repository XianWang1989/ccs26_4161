
import OpenGL.GL as gl
import numpy as np
import cv2

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape

    if flip:
        image = np.flipud(image)  # Flip vertically if needed

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main loop portion for loading image
image = cv2.imread('../imtools/image/ummagumma.jpg', cv2.IMREAD_UNCHANGED)
if image is not None:
    if image.shape[2] == 4:  # Check for alpha channel
        image = image[:, :, :3]  # Discard alpha channel if needed
    swap_rb(image)  # Swap R and B channels
    tx_id = tx2gpu(image)
else:
    print("Error loading image.")
