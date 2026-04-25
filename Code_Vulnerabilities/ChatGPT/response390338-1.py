
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Use OpenCV for reading images

def load_texture(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # If the image is loaded correctly
    if image is None:
        raise Exception("Could not load image: {}".format(image_path))

    # Check the shape of the image before proceeding
    print(f"Image shape: {image.shape}")  # Should be (height, width, channels)

    # Swap RB channels if necessary
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optionally rotate the image if needed
    # image = np.rot90(image)  # Uncomment to apply rotation

    return image

def tx2gpu(image, unit=0):
    gl.glActiveTexture(gl.GL_TEXTURE0 + unit)
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Flip the image vertically because OpenGL and image coordinate systems differ
    image = np.flipud(image)

    # Define the texture
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.shape[1], image.shape[0],
                     0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
    gl.glEnd()

if __name__ == '__main__':
    glfw.init()
    win = glfw.create_window(800, 800, "OpenGL Texture", None, None)
    glfw.make_context_current(win)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = load_texture('path/to/your/image.jpg')  # Replace with your image path
    tx_id = tx2gpu(image)

    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glEnable(gl.GL_TEXTURE_2D)

        # Referencing the texture
        gl.glBindTexture(gl.GL_TEXTURE_2D, tx_id)

        square(2)  # Draw the square
        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()
