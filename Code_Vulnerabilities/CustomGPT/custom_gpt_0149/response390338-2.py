
# Rotate the image
image = np.rot90(image, k=1)  # Rotate 90 degrees counter-clockwise
image = np.flipud(image)       # Adjust orientation correctly
