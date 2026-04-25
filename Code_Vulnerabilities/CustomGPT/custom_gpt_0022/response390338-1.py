
def square(scale=1.0, solid=True):
    s = scale * 0.5
    if solid:
        gl.glBegin(gl.GL_TRIANGLE_FAN)
    else:
        gl.glBegin(gl.GL_LINE_LOOP)

    gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
    gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
    gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
    gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)

    gl.glEnd()
