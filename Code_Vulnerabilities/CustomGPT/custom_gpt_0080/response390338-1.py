
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from cv2 import imread

def load_and_prepare_texture(image_path):
    image = imread(image_path)
    if image is None:
        print("Failed to load image.")
        return None

    # Swap Red and Blue channels
    image = image[..., ::-1]  # BGR to RGB

    # Check dimensions (power of two)
    yres, xres, _ = image.shape
    if (xres & (xres - 1)) != 0 or (yres & (yres - 1)) != 0:
        print("Warning: Texture dimensions should ideally be powers of two.")

    return image

def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Flip the image vertically only if necessary
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB,
                    gl.GL_UNSIGNED_BYTE, np.flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# In main function, handle image loading:
if __name__ == '__main__':
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello", None, None)
    glfw.glfwMakeContextCurrent(win)

    image = load_and_prepare_texture('../imtools/image/ummagumma.jpg')
    if image is not None:
        tx_id = tx2gpu(image)

    # Main loop and rendering...
