
import sys
import glfw
import OpenGL.GL as gl
import numpy as np
import cv2  # Use OpenCV for image loading

def swap_rb(image):
    # Swap the Red and Blue channels of the image.
    r = image[:,:,0].copy()
    image[:,:,0] = image[:,:,2]
    image[:,:,2] = r
    return image

def tx2gpu(image):
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Flip the image vertically before sending it to the GPU
    image = np.flipud(image)
    # Ensure the image is in the correct format (RGB)
    image = swap_rb(image)
    height, width, _ = image.shape

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 800, "OpenGL Texture Example", None, None)
    glfw.make_context_current(window)

    # Load your image using OpenCV
    image = cv2.imread('path/to/your/image.jpg')  # Update the image path
    if image is None:
        print("Image not loaded!")
        sys.exit(1)

    tx_id = tx2gpu(image)

    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tx_id)

        # Define square vertices and texture coordinates
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glTexCoord2f(0.0, 0.0); gl.glVertex2f(-1.0, -1.0)
        gl.glTexCoord2f(0.0, 1.0); gl.glVertex2f(-1.0,  1.0)
        gl.glTexCoord2f(1.0, 1.0); gl.glVertex2f( 1.0,  1.0)
        gl.glTexCoord2f(1.0, 0.0); gl.glVertex2f( 1.0, -1.0)
        gl.glEnd()

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        gl.glDisable(gl.GL_TEXTURE_2D)

        glfw.swap_buffers(window)
        glfw.poll_events()

    # Cleanup
    gl.glDeleteTextures(1, [tx_id])
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
