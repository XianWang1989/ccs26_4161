
import cv2  # Make sure OpenCV is installed
import OpenGL.GL as gl
import numpy as np

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Get image dimensions
    yres, xres, cresc = image.shape
    if flip:
        image = np.flipud(image)  # Flip the image vertically if needed

    # Ensure we have the correct color format
    if cresc == 3:  # RGB
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    elif cresc == 4:  # RGBA
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, xres, yres, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Load the image with OpenCV
image = cv2.imread('../imtools/image/ummagumma.jpg')
if image is None:
    print("Error loading image")
else:
    if rgb_flag: swap_rb(image)  # Ensure the colors are correctly ordered
    tx_id = tx2gpu(image)
