
import cv2  # Make sure you use OpenCV for reading images
import numpy as np
import OpenGL.GL as gl

def load_and_prepare_texture(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image could not be found or opened.")

    # Ensure the image is in RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Rotate the image but preserve the correct orientation
    rotated_image = np.rot90(image)  # Use the desired rotation

    # Flip the image for OpenGL compatibility
    flipped_image = np.flipud(rotated_image)

    return flipped_image

def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Get image dimensions
    yres, xres, _ = image.shape

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
