
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Ensure you have OpenCV installed

def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found: {image_path}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    image = np.flipud(image)  # Flip the image vertically
    return image

def tx2gpu(image, unit=0):
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s,  s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f( s,  s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f( s, -s, 0)
    gl.glEnd()

# Main program
if __name__ == '__main__':
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    image = load_texture('path/to/your/image.jpg')
    texture_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.bindTexture(gl.GL_TEXTURE_2D, texture_id)
        square(2)
        gl.bindTexture(gl.GL_TEXTURE_2D, 0)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
