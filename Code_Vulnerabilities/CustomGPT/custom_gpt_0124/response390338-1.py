
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

def load_texture(image_path):
    image = imread(image_path)
    if not rgb_flag: 
        swap_rb(image)
    image = np.flipud(image)  # Flip the image vertically
    return tx2gpu(image)

def main():
    glfw.glfwInit()
    win = glfw.glfwCreateWindow(800, 800, "Texture Example")
    glfw.glfwMakeContextCurrent(win)
    glfw.glfwSwapInterval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    tx_id = load_texture('../imtools/image/ummagumma.jpg')  # Adjust path accordingly

    while not glfw.glfwWindowShouldClose(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        txrefer(0)  
        glfw.glfwSwapBuffers(win)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(win)
    glfw.glfwTerminate()

def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

if __name__ == '__main__':
    main()
