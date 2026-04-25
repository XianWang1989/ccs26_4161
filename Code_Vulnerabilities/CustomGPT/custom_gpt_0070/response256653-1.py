
from PIL import Image

# Create a simple JPEG image
def create_test_jpeg(filename):
    img = Image.new('RGB', (100, 100), color = (155, 0, 0))
    img.save(filename, format='JPEG')

# Test to open the JPEG image
def test_jpeg_support(filename):
    try:
        with Image.open(filename) as img:
            img.show()
            print(f"Opened {filename} successfully.")
    except Exception as e:
        print(f"Failed to open {filename}: {e}")

if __name__ == "__main__":
    test_filename = "test_image.jpg"
    create_test_jpeg(test_filename)
    test_jpeg_support(test_filename)
