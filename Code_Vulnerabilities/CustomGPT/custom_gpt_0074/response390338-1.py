
def tx2gpu(image, unit=0):
    # Activating the texture unit
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)  # Generate texture ID
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Handling image data
    yres, xres, cresc = image.shape
    # If your images might have an alpha channel, ensure you handle it
    if cresc == 4:  # If image has alpha channel
        format = gl.GL_RGBA
    else:
        format = gl.GL_RGB

    # Flip vertical axis
    from numpy import flipud
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, format, xres, yres, 0, format, gl.GL_UNSIGNED_BYTE, flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)  # Unbind texture
    return texture_id

# Usage
image = imread('../imtools/image/ummagumma.jpg')
if not rgb_flag: 
    image = swap_rb(image)  # Swap colors if necessary
# Make sure to comment or remove the rotation for testing
# image = np.rot90(image)  # Only if necessary, as it may cause distortion
tx_id = tx2gpu(image)
