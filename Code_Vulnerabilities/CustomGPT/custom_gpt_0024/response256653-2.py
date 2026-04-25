
from PIL import Image

def test_jpeg_support():
    try:
        # Create a simple RGB image
        img = Image.new('RGB', (100, 100), color = 'red')

        # Save as JPEG
        img.save('test_image.jpg', 'JPEG')
        print("JPEG image created successfully!")

        # Open the JPEG image
        with Image.open('test_image.jpg') as opened_img:
            print("Opened JPEG image successfully!")
            opened_img.show()  # This will display the image using the default viewer

    except Exception as e:
        print(f"An error occurred: {e}")

test_jpeg_support()
