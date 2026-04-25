
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Use OpenCV to read images

def load_texture(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise Exception(f"Could not load image: {image_path}")

    # Ensure image is in RGB format by converting from BGR (OpenCV default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flip the image vertically if OpenGL standard is needed
    image = np.flipud(image)

    # Generate texture
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Load texture into OpenGL
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture

    return texture_id

# Your square drawing function remains unchanged

if __name__ == '__main__':
    # Initialize GLFW and create window
    if not glfw.init():
        sys.exit()
    window = glfw.create_window(800, 800, "OpenGL Texturing", None, None)
    glfw.make_context_current(window)

    # Load the texture
    texture_id = load_texture('path/to/your/image.jpg')

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(texture_id)  # Call your texture bind function
        square(2)            # Draw the square
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
