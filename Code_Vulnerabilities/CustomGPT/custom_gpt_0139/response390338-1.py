
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Assuming you are using OpenCV to load images

def load_texture(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Check if image is loaded properly
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    # Ensure image is in RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flip the image vertically, as OpenGL expects the origin at the bottom left
    image = np.flipud(image)

    # Generate texture ID
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture

    return texture_id

# Main function
if __name__ == '__main__':
    glfw.init()
    window = glfw.create_window(800, 800, "OpenGL Texture Example", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('path_to_your_image.jpg')  # Path to your image

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # Bind the texture and draw the square or any other geometry here
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        # Call your drawing function...

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()
