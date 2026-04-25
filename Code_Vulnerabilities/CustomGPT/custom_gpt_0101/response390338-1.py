
# Ensure proper libraries are imported
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread, rgb_flag, swap_rb
from txio import tx2gpu, txrefer

# Initialize GLFW
glfw.glfwInit()
win = glfw.glfwCreateWindow(800, 800, "Hello")
glfw.glfwMakeContextCurrent(win)
glfw.glfwSwapInterval(1)
gl.glClearColor(0.75, 0.75, 0.75, 1.0)

# Load image and send to GPU
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag:
    swap_rb(image)
tx_id = tx2gpu(image)

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)
    square(2)
    txrefer(0)
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()

# Cleanup
glfw.glfwDestroyWindow(win)
glfw.glfwTerminate()

# Define square function
def square(scale=1.0, color=None, solid=True):
    s = scale * .5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    if color is not None:
        for i in range(4):
            gl.glColor3f(*color[i][:3])
            gl.glVertex3f(s * (-1 if i % 2 == 0 else 1), s * (1 if i < 2 else -1), 0)
    else:
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()
