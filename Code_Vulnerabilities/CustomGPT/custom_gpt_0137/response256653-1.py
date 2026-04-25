
from PIL import Image

def test_jpeg_support():
    # Create a simple RGB image
    img = Image.new("RGB", (100, 100), color="red")

    # Save the image in JPEG format
    try:
        img.save("test_image.jpg", "JPEG")
        print("JPEG image saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving JPEG image: {e}")

    # Try to open the JPEG image
    try:
        jpg_image = Image.open("test_image.jpg")
        jpg_image.show()  # This will attempt to display the image
        print("JPEG image opened successfully.")
    except Exception as e:
        print(f"An error occurred while opening JPEG image: {e}")

if __name__ == "__main__":
    test_jpeg_support()
