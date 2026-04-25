
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Make sure you have OpenCV installed

def load_texture(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Could not load image.")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = np.flipud(image)  # Flip the image vertically

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Load texture image into the GPU
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    return texture_id

# Example of setting up OpenGL and using the load_texture function
if __name__ == '__main__':
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800, 600, "OpenGL Texture", None, None)
    glfw.make_context_current(window)

    texture_id = load_texture('path_to_your_image.jpg')  # Update with your image path

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Use texture
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        # Draw your textured square here...

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()
