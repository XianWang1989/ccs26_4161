
# Open the file in 'r+b' mode (read and write in binary)
with open('example.txt', 'r+b') as file:
    # Define the position and the string you want to write
    position = (4, 0)  # Start replacing from index 4
    replacement_string = '01234'

    # Move to the desired position in the file
    file.seek(position[0])

    # Write the new bytes; ensure to encode the string if necessary
    file.write(replacement_string.encode('utf-8'))
