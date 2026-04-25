def tx2gpu(image, flip=True, unit=0):
    import OpenGL.GL as gl
    from numpy import flipud
    if image.shape[2] != 3:
        raise ValueError("Image must be RGB with 3 channels")

    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)

    yres, xres, cres = image.shape
    upload_image = flipud(image) if flip else image

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, upload_image)
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    return texture_id
