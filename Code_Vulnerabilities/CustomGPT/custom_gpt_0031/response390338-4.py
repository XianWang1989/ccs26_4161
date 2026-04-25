
def tx2gpu(image, flip=True, unit=0):
    gl.glActiveTexture(unit_symbols[unit])
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

    yres, xres, cres = image.shape
    from numpy import flipud
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, xres, yres, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, flipud(image))

    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return texture_id

def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    if type(color) != type(None):
        if solid: 
            gl.glBegin(gl.GL_TRIANGLE_FAN)
        else:
            gl.glBegin(gl.GL_LINE_LOOP)
        gl.glColor3f(*color[0][:3]); gl.glVertex3f(-s, -s, 0)
        gl.glColor3f(*color[1][:3]); gl.glVertex3f(-s, s, 0)
        gl.glColor3f(*color[2][:3]); gl.glVertex3f(s, s, 0)
        gl.glColor3f(*color[3][:3]); gl.glVertex3f(s, -s, 0)
    else:    
        if solid: 
            gl.glBegin(gl.GL_TRIANGLE_FAN)
        else:
            gl.glBegin(gl.GL_LINE_LOOP)
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glEnd()
