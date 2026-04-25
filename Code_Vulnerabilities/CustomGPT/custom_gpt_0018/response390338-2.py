
# Assuming an image is loaded using OpenCV
import cv2  # OpenCV for loading the image

image = cv2.imread('path_to_image.jpg')
if image is None:
    print("Error: Image could not be loaded.")
else:
    # Convert color from BGR (OpenCV default) to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Optionally rotate the image
    image = np.rot90(image, k=1)  # Rotate 90 degrees clockwise
    tx_id = tx2gpu(image)

# In the rendering loop
while not glfw.glfwWindowShouldClose(win):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    txrefer(tx_id)
    square(2)  # Draw your textured square
    txrefer(0)
    glfw.glfwSwapBuffers(win)
    glfw.glfwPollEvents()
