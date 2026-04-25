
import glfw
import OpenGL.GL as gl
import numpy as np
from PIL import Image

def load_texture(filename):
    # Load image
    img = Image.open(filename)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip vertically if needed
    img_data = np.array(img)

    # Generate texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Load texture data
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, img_data.shape[1], img_data.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, img_data)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# OpenGL initialization and rendering loop
if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "Texture Example", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('your_image.jpg')  # Replace with your image path

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Bind and use the texture
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        # Call a function to draw a square here

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
