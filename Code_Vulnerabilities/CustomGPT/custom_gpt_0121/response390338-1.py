
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # OpenCV for image loading

# Texture loading function
def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Could not load image")

    # Swap R and B channels
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flip the image vertically
    image = np.flipud(image)

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Send the image data to OpenGL
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Function to draw a textured square
def draw_textured_square(texture_id):
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-0.5, -0.5, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-0.5,  0.5, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f( 0.5,  0.5, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f( 0.5, -0.5, 0)
    gl.glEnd()
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "Textured Square", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture("path/to/your/image.jpg")

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        draw_textured_square(texture_id)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()
