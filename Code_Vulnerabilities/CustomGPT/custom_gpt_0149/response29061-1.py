
import os

# Get the current file's absolute path
file_path = os.path.abspath(__file__)

# Extract the directory path
directory_path = os.path.dirname(file_path)

print(directory_path)
