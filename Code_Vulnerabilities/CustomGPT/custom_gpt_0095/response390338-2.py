
image = np.rot90(image, k=1)  # Rotate 90 degrees
# Check dimensions after rotation
print(image.shape)  # This should match (height, width, channels)
