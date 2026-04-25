
import os

# Get the full path of the current file
current_file_path = os.path.abspath(__file__)

# Extract the directory path
current_directory = os.path.dirname(current_file_path)

print(current_directory)
