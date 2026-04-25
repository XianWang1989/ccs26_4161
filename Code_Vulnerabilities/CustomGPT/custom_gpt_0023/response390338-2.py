
# If your images may include an alpha channel
if image.shape[2] == 4:  # RGBA
    image = image[:, :, :3]  # Ignore the alpha channel
