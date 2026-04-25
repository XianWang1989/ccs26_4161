
if image.ndim == 3 and image.shape[2] == 4:
    image = image[:, :, :3]  # Remove alpha channel
