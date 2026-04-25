
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Retrieve the directory path
current_directory = os.path.dirname(current_file_path)

# Print the directory path
print(current_directory)
