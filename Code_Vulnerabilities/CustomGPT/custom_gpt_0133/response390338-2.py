
def square(scale=1.0, color=None, solid=True):
    s = scale * 0.5
    if color is not None:
        if solid: 
            gl.glBegin(gl.GL_TRIANGLE_FAN)
        else:
            gl.glBegin(gl.GL_LINE_LOOP)
        for vertex in color:
            gl.glColor3f(*vertex[:3])
            gl.glVertex3f(-s, -s, 0)
        gl.glEnd()
    else:    
        if solid: 
            gl.glBegin(gl.GL_TRIANGLE_FAN)
        else:
            gl.glBegin(gl.GL_LINE_LOOP)

        # Ensure texture coordinates and vertex positions match
        gl.glTexCoord2f(0, 0); gl.glVertex3f(-s, -s, 0)  # Bottom left
        gl.glTexCoord2f(0, 1); gl.glVertex3f(-s, s, 0)   # Top left
        gl.glTexCoord2f(1, 1); gl.glVertex3f(s, s, 0)    # Top right
        gl.glTexCoord2f(1, 0); gl.glVertex3f(s, -s, 0)   # Bottom right
        gl.glEnd()
