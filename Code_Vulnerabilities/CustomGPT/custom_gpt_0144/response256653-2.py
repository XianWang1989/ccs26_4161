from PIL import features
print("JPEG support:", features.check('jpeg'))
print("ZLIB support:", features.check('zlib'))
