
import os

# Get the full path of the current file
full_path = os.path.abspath(__file__)

# Retrieve the directory path
directory_path = os.path.dirname(full_path)

print(directory_path)
