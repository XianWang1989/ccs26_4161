
import cv2
import numpy as np
import OpenGL.GL as gl

def load_texture(image_path):
    # Load image with OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise Exception("Could not load image")

    # Convert RGB to BGR for OpenGL
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flip the image vertically
    image = np.flipud(image)

    # Generate texture ID
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Upload texture data
    height, width, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind the texture
    return texture_id

# Usage example
texture_id = load_texture('../imtools/image/ummagumma.jpg')
