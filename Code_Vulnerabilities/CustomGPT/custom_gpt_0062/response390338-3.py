
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from imio import imread  # Assuming this imports correctly

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = imread('path_to_image.jpg')
    texture_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        txrefer(texture_id)
        square(1.0)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
