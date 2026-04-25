
import os

# Get the full path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory path of the current file
current_directory = os.path.dirname(current_file_path)

print(current_directory)
