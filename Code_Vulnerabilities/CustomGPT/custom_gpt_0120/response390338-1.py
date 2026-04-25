
import numpy as np
import glfw
import OpenGL.GL as gl
import cv2  # Import OpenCV for image loading

def swap_rb(mat):
    mat[..., [0, 2]] = mat[..., [2, 0]]  # Swap Red and Blue channels
    return mat

def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, np.flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def load_and_prepare_texture(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Could not load image")
    image = swap_rb(image)  # Swap RGB channels
    return image

# Example main function to demonstrate loading and displaying the texture
if __name__ == "__main__":
    if not glfw.init():
        raise Exception("GLFW cannot be initialized")
    window = glfw.create_window(800, 800, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window cannot be created")

    glfw.make_context_current(window)

    # Load and prepare texture
    texture_image = load_and_prepare_texture('path_to_your_image.jpg')
    tx_id = tx2gpu(texture_image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)  # Bind the texture
        square(2)       # Draw the square with the texture
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
