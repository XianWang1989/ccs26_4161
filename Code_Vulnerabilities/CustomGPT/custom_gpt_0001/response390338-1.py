
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from PIL import Image  # Use PIL to read images easily

def swap_rb(mat):
    X = mat[:,:,2].copy()
    mat[:,:,2] = mat[:,:,0]
    mat[:,:,0] = X
    return mat

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)

    yres, xres, cres = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def main():
    if not glfw.init():
        return

    win = glfw.create_window(800, 800, "Texture Example", None, None)
    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    # Load the image using PIL
    img = Image.open('path_to_your_image.jpg')
    img = img.convert('RGB')  # Ensure RGB format
    image_data = np.array(img)

    # Rotate image (optional, only if required)
    # image_data = np.rot90(image_data)  # Uncomment if needed

    # Swap RGB channels
    image_data = swap_rb(image_data)

    # Send to GPU
    tx_id = tx2gpu(image_data)

    # Main loop
    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # Call your square function with textures here
        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.destroy_window(win)
    glfw.terminate()

if __name__ == '__main__':
    main()
