
# Open the file in 'r+b' mode to allow reading and writing
with open('your_file.txt', 'r+b') as file:
    # Define the position to seek to (4, 0) means position 4
    position = 4
    # Seek to the position
    file.seek(position)
    # Define the new string you want to write
    new_string = b'01234'
    # Write the new string to the file, replacing existing bytes
    file.write(new_string)

# Output to check the result
with open('your_file.txt', 'r') as file:
    content = file.read()
    print(content)  # Should display: this01234ethingasperfectlygood.
