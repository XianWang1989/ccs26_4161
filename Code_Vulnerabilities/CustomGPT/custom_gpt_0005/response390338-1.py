
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb

def load_texture(image_path):
    image = imread(image_path)
    if not rgb_flag:
        swap_rb(image)
    return tx2gpu(image)

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape
    if flip:
        image = np.flipud(image)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main OpenGL loop
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)  # Bind the texture
    square(2)       # Draw the square
    txrefer(0)      # Unbind the texture
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
