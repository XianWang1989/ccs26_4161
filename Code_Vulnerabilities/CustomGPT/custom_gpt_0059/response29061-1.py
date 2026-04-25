
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory name from the file path
current_directory = os.path.dirname(current_file_path)

print(current_directory)
