
def tx2gpu(image, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Ensure 'image' has the shape (height, width, channels)
    yres, xres, cres = image.shape

    if cres == 4:  # Handle RGBA format
        gl_format = gl.GL_RGBA
    elif cres == 3:  # Handle RGB format
        gl_format = gl.GL_RGB
    else:
        raise ValueError("Unsupported image format")

    # Flip the image vertically
    flipped_image = np.flipud(image)

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl_format, xres, yres, 0, gl_format, gl.GL_UNSIGNED_BYTE, flipped_image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
