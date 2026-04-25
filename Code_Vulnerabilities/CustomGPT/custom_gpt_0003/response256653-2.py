
from PIL import Image

# Open a JPEG image file
try:
    img = Image.open('example.jpg')
    img.show()  # Display the image
    # Convert image to grayscale
    grayscale_img = img.convert('L')
    grayscale_img.save('example_gray.jpg')  # Save as a new file
    print("JPEG image processed successfully!")
except Exception as e:
    print("An error occurred:", e)
