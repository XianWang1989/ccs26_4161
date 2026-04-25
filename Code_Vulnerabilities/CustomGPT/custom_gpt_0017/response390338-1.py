
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Make sure to use OpenCV for image loading

def load_texture(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Failed to load image.")

    # Convert image to RGB and swap RB channels
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.flipud(image)  # Flip the image if necessary (adjust as required)

    # Generate texture ID and bind it
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Upload texture data to GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 
                    0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

if __name__ == '__main__':
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800, 800, "OpenGL Example", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('../imtools/image/ummagumma.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Add code to draw your textured square here...

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
