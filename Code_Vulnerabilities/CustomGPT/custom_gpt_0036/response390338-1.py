
import numpy as np
import OpenGL.GL as gl
from OpenGL.GL import shaders
import glfw
import cv2  # Ensure you have OpenCV installed

def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    # Swap red and blue channels
    image = swap_rb(image)

    # Flip the image vertically to make the origin bottom-left
    image = np.flipud(image)

    # Generate and bind the texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Upload the texture to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind the texture
    return texture_id

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)

    # Set texture coordinates and vertices
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)  # Top-left
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)   # Top-right
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)  # Bottom-right
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0) # Bottom-left

    gl.glEnd()

def swap_rb(mat):
    mat = mat.copy()  # Make a copy to avoid in-place modification
    mat[..., 0], mat[..., 2] = mat[..., 2], mat[..., 0]  # Swap red and blue channels
    return mat
