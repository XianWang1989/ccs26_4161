
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Using OpenCV for image loading

def load_texture(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Image not found")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    return image

def tx2gpu(image, flip=True):
    # Upload texture to GPU
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Flip image vertically if required
    if flip:
        image = np.flipud(image)

    # Check image shape
    if image.ndim != 3 or image.shape[2] != 3:
        raise Exception("Invalid image shape, must be (height, width, channels) and have 3 channels.")

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def display_texture(texture_id):
    gl.glEnable(gl.GL_TEXTURE_2D)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Render square with texture
    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0, 0); gl.glVertex2f(-0.5, -0.5)
    gl.glTexCoord2f(1, 0); gl.glVertex2f(0.5, -0.5)
    gl.glTexCoord2f(1, 1); gl.glVertex2f(0.5, 0.5)
    gl.glTexCoord2f(0, 1); gl.glVertex2f(-0.5, 0.5)
    gl.glEnd()

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    gl.glDisable(gl.GL_TEXTURE_2D)

def main():
    # Initialize GLFW and OpenGL context...
    glfw.init()
    window = glfw.create_window(800, 600, "OpenGL Texture", None, None)
    glfw.make_context_current(window)

    # Load image
    image = load_texture('path_to_image.jpg')

    # Create texture
    texture_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        display_texture(texture_id)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
