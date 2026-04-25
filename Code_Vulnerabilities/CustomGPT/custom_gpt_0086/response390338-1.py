
import cv2  # Make sure you have this library
import OpenGL.GL as gl
import numpy as np

def load_texture(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optional: Rotate if needed
    # image = np.rot90(image)  # Uncomment if you need to rotate

    # Flip the image for OpenGL (because of different Y-axis origins)
    image = np.flipud(image)

    yarn, xres, yres = image.shape
    texture_id = gl.glGenTextures(1)

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# In your main loop:
image_path = '../imtools/image/ummagumma.jpg'
texture_id = load_texture(image_path)

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(texture_id)
    square(2)
    txrefer(0)
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
