
import OpenGL.GL as gl
import numpy as np
import cv2  # Ensure you have OpenCV for image loading

def load_texture(filename):
    # Load the image using OpenCV
    image = cv2.imread(filename)

    # Check if the image was loaded correctly
    if image is None:
        print("Error: Could not load image.")
        return None

    # Convert the image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    yres, xres, _ = image.shape

    # Check if dimensions are powers of two
    if not (xres & (xres - 1) == 0 and yres & (yres - 1) == 0):
        print("Warning: Texture dimensions are not powers of two.")

    # Create and bind the texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Configure texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Upload the texture data
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, np.flipud(image))

    # Return the texture ID
    return texture_id
