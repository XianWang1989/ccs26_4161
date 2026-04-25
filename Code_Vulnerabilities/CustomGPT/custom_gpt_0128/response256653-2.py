
import PIL
print(PIL.__version__)  # Should match your installed Pillow version
print("JPEG Support:", "JPEG" in PIL.features.check("jpeg"))
