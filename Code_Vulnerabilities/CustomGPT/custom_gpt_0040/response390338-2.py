
def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)

    gl.glTexCoord2f(0.0, 0.0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0.0, 1.0); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1.0, 1.0); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1.0, 0.0); gl.glVertex3f(s, -s, 0)

    gl.glEnd()
