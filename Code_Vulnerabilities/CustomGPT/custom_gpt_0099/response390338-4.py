
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2

def load_texture(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise Exception("Could not load image")

    if image.shape[2] == 4:  # RGBA
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

    yres, xres, _ = image.shape

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, np.flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main loop integration
texture_id = load_texture('../imtools/image/ummagumma.jpg')

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(texture_id)
    square(2)
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
