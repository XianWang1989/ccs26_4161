
import os

# Get the full path of the current file
current_file_path = os.path.abspath(__file__)

# Retrieve the directory path of the current file
current_directory_path = os.path.dirname(current_file_path)

print("Current file path:", current_file_path)
print("Current directory path:", current_directory_path)
