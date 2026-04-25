
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    if flip:
        image = np.flipud(image)

    # Ensure the image is in the proper format (RGB)
    if image.shape[2] != 3:
        raise ValueError("Image must have 3 channels (RGB).")

    yres, xres, _ = image.shape
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

# Example where you would call tx2gpu
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag:
    image = swap_rb(image)

# Rotate images if needed and adjust dimensions post-rotation
image = np.rot90(image)  # Rotate
if image.shape[0] % 2 != 0 or image.shape[1] % 2 != 0:
    raise ValueError("Texture dimensions should be powers of two.")

tx_id = tx2gpu(image)

while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id); square(2); txrefer(0)
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
