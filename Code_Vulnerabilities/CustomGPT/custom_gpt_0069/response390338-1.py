
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb  # Ensure these handle RGB correctly
from txio import tx2gpu, txrefer

def load_and_prepare_texture(image_path):
    image = imread(image_path)
    if not rgb_flag:
        image = swap_rb(image)
    return tx2gpu(image)

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

def main():
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Hello", None, None)
    glfw.glfwMakeContextCurrent(win)

    texture_id = load_and_prepare_texture('../imtools/image/ummagumma.jpg')

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(texture_id)
        square(2)
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()

if __name__ == '__main__':
    main()
