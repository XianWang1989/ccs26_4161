
import os

# Get the full path of the current file
file_path = os.path.abspath(__file__)

# Get the directory path
directory_path = os.path.dirname(file_path)

print(directory_path)
