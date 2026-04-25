
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Use flipud to flip image vertically
    if flip:
        image = np.flipud(image)

    # Catch possible errors if the image is not in the right format
    try:
        yres, xres, cres = image.shape
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    except ValueError as e:
        print("Error uploading texture:", e)
        return None

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Main Loop Example
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    txrefer(tx_id)  # Bind texture
    square(2)       # Draw square
    taxrefer(0)     # Unbind texture

    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
