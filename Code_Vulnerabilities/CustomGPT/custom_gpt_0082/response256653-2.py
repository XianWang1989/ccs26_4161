
from PIL import Image

try:
    img = Image.open('example.jpg')  # Replace with your JPEG file
    img.show()  # Display the image
    img.save('output.png')  # Save as PNG to check functionality
    print("JPEG loaded and saved successfully!")
except Exception as e:
    print(f"Error: {e}")
