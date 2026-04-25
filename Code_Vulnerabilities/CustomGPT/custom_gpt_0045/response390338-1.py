
if __name__ == '__main__':
    import sys
    import glfw
    import OpenGL.GL as gl
    import numpy as np
    import cv2  # Ensure OpenCV is imported for image reading

    from square import square
    from txio import tx2gpu, txrefer

    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW cannot be initialized!")

    win = glfw.create_window(800, 800, "Hello", None, None)
    if not win:
        glfw.terminate()
        raise Exception("GLFW window cannot be created!")

    glfw.make_context_current(win)
    glfw.swap_interval(1)
    gl.glClearColor(0.75, 0.75, 0.75, 1.0)

    # Load image using OpenCV
    image = cv2.imread('../imtools/image/ummagumma.jpg')

    # Check if the image was loaded correctly
    if image is None:
        raise Exception("Image not found or could not be loaded.")

    # Correct the color channels (BGR to RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optionally flip the image vertically (Y-axis flip)
    image = np.flipud(image)

    # Send the image to the GPU
    tx_id = tx2gpu(image)

    while not glfw.window_should_close(win):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        txrefer(tx_id)  
        square(2)  
        txrefer(0)  
        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.destroy_window(win)
    glfw.terminate()
