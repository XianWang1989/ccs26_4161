
error = gl.glGetError()
if error != gl.GL_NO_ERROR:
    print(f"OpenGL Error: {error}")
