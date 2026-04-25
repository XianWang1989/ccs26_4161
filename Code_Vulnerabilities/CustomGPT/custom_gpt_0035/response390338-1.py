
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)  # Change here
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)  # Change here
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape

    from numpy import flipud
    if flip:  # Only flip if needed
        image = flipud(image)

    # Ensure correct number of channels
    if cres == 3:  # RGB
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image)
    elif cres == 4:  # RGBA
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, xres, yres, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
