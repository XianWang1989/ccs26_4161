
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

        # Here make sure to adjust based on image flipping and dimensions
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, -s, 0)  # Bottom-left
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, s, 0)    # Top-left
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, s, 0)      # Top-right
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, -s, 0)     # Bottom-right

    gl.glEnd()
