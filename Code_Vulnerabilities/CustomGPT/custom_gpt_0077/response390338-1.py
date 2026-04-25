
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
from PIL import Image

def load_texture(image_path):
    img = Image.open(image_path).convert('RGB')
    img_data = np.array(img)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, img_data.shape[1], img_data.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, img_data)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def render_square(texture_id):
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex2f(-0.5, -0.5)
    gl.glTexCoord2f(1, 0); gl.glVertex2f(0.5, -0.5)
    gl.glTexCoord2f(1, 1); gl.glVertex2f(0.5, 0.5)
    gl.glTexCoord2f(0, 1); gl.glVertex2f(-0.5, 0.5)
    gl.glEnd()
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

def main():
    glfw.init()
    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('path_to_your_image.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        render_square(texture_id)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == '__main__':
    main()
