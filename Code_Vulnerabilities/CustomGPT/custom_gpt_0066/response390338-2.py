
if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl
    import numpy as np
    from imio import imread, rgb_flag, swap_rb
    from txio import tx2gpu, txrefer

    glfw.init()
    win = glfw.create_window(800, 800, "OpenGL Texture Example", None, None)
    glfw.make_context_current(win)

    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    image = imread('../imtools/image/ummagumma.jpg')
    if not rgb_flag: swap_rb(image)

    tx_id = tx2gpu(image)  # Load image to GPU

    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)
        square(2)
        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.destroy_window(win)
    glfw.terminate()
