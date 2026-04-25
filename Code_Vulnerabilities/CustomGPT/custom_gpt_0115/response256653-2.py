
from PIL import Image, ImageDraw

# Create a new image with RGB mode
width, height = 200, 100
image = Image.new("RGB", (width, height), "blue")

# Draw something on the image
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Hello, JPEG!", fill="white")

# Save as JPEG and PNG
image.save("output_image.jpg", "JPEG")
image.save("output_image.png", "PNG")

print("Images saved as output_image.jpg and output_image.png")
