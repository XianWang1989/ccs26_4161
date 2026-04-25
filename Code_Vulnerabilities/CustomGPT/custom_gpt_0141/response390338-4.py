
def square(scale=1.0):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)  # Bottom left
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)   # Top left
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)    # Top right
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)   # Bottom right
    gl.glEnd()
