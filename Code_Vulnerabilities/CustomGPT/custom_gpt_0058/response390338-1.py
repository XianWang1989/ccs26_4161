
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    # Assuming the image is loaded in HxWxC (Height x Width x Channels) format
    yres, xres, cres = image.shape

    if flip:
        image = np.flipud(image)

    # Check image shape to ensure it's valid
    print(f"Image shape: {image.shape}, dtype: {image.dtype}")

    # Use correct format based on the channels of input image
    if cres == 3:
        gl_format = gl.GL_RGB
    elif cres == 4:
        gl_format = gl.GL_RGBA
    else:
        raise ValueError("Unsupported channel count: must be 3 or 4.")

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl_format, xres, yres, 0, gl_format, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
