
import OpenGL.GL as gl
import numpy as np
from PIL import Image

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Check if the image is in a valid format
    if image.ndim == 2:  # Grayscale image
        image = np.stack((image,)*3, axis=-1)  # Convert to RGB

    # Ensure correct channel ordering (RGB to BGR)
    if image.shape[2] == 3:  # RGB image
        image = image[:,:,[2, 1, 0]]  # Swap R and B channels

    yres, xres, _ = image.shape
    if flip:
        image = np.flipud(image)  # Flip the image vertically if needed

    # Upload texture to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Example usage
image_path = '../imtools/image/ummagumma.jpg'
image = Image.open(image_path)  # Use PIL to read image
image = np.array(image)  # Convert image to a numpy array
tx_id = tx2gpu(image)
