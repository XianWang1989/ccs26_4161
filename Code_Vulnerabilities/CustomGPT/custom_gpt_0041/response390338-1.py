
import cv2  # Use OpenCV for image loading
import numpy as np
import glfw
import OpenGL.GL as gl

# Swapping red and blue channels
def swap_rb(mat):
    mat[..., 0], mat[..., 2] = mat[..., 2], mat[..., 0]
    return mat

# Load and prepare the texture
def load_texture(image_path):
    image = cv2.imread(image_path)  # Load image
    if image is None:
        raise Exception("Image not found!")

    image = swap_rb(image)  # Swap channels
    # Flip the image vertically if needed
    image = np.flipud(image)
    return image

# Texture loading function
def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main function setup
if __name__ == '__main__':
    if not glfw.init():
        raise Exception("GLFW cannot be initialized")

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    # Load texture
    image = load_texture('../imtools/image/ummagumma.jpg')
    tx_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)  # Bind the texture
        square(2)  # Draw the square
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
