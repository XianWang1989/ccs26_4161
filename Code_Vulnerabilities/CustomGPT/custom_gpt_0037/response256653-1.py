
from PIL import Image

# Open a JPEG image
img = Image.open("example.jpg")

# Display the image
img.show()

# Convert the image to another format
img.convert("L").save("example_gray.jpg")

# Resize the image
resized_img = img.resize((200, 200))
resized_img.save("example_resized.jpg")
