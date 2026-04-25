
import glfw
import OpenGL.GL as gl
import numpy as np
from PIL import Image

# Function to load image and swap red and blue channels
def load_texture(image_path):
    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip vertically
    image_data = np.array(list(image.getdata()), np.uint8)
    return image_data, image.size

# Function to create a square with texture
def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

# Main function to set up OpenGL and render the square
def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)
    gl.glEnable(gl.GL_TEXTURE_2D)

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Load texture
    image_data, (width, height) = load_texture('path/to/your/image.jpg')
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image_data)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        square(2.0)  # Draw the textured square
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
