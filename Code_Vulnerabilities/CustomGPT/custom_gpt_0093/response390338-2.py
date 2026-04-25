
image = np.rot90(image, k=1)  # Rotate 90 degrees counterclockwise

# Adjust texture coordinates if needed depending on the rotation
# Example adjustment knows you're using glTexCoord2f
