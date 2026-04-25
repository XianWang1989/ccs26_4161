
def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    gl.glBegin(gl.GL_TRIANGLE_FAN)

    if color is not None:
        for i in range(4):
            gl.glColor3f(*color[i][:3])
            gl.glVertex3f(-s if i % 2 == 0 else s, -s if i < 2 else s, 0)
    else:
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)

    gl.glEnd()
