
import glfw
import OpenGL.GL as gl
import numpy as np
from OpenCV import imread

def load_texture(image_path):
    image = imread(image_path)
    if image is None:
        print("Failed to load image")
        return None

    # Swap Red and Blue channels
    image = image[..., ::-1]

    height, width, channels = image.shape

    # Flip the image vertically
    image = np.flipud(image)

    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Create texture
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture

    return texture_id

# In your main function, replace this to load textures
if __name__ == '__main__':
    # Initialize GLFW, create window, etc.

    texture_id = load_texture('path/to/your/image.jpg')

    while not glfw.glfwWindowShouldClose(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        # Draw your textured square here
        draw_square()  # Implement your square drawing logic

        glfw.glfwSwapBuffers(window)
        glfw.glfwPollEvents()

    glfw.glfwDestroyWindow(window)
    glfw.glfwTerminate()
