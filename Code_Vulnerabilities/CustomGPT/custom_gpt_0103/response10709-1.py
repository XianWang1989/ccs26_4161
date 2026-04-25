
# Define the file path and the bytes to write
file_path = 'example_file.txt'  # Change this to your file path
replacement_bytes = b'01234'      # Bytes to write
offset = 4                         # Position to replace

# Open the file in 'r+b' mode to read and write binary data
with open(file_path, 'r+b') as f:
    # Move the cursor to the specified offset
    f.seek(offset)
    # Write the replacement bytes
    f.write(replacement_bytes)

print("Replacement done.")
