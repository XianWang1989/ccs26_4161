
import cv2  # Ensure you've imported OpenCV

def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape

    if flip:  # Check if flipping is needed
        image = np.flipud(image)  # Flipping the image upside down

    # Ensure the image is in the correct format for OpenGL
    if cres == 3:  # Assuming RGB
        format = gl.GL_RGB
    else:
        print("Unexpected image channels: ", cres)
        return None

    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, format, xres, yres, 0, format, gl.GL_UNSIGNED_BYTE, image)

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id
