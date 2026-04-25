
def replace_bytes_in_file(file_path, position, new_string):
    # Ensure that the new_string's length is not greater than the length of the segment being replaced
    with open(file_path, 'r+b') as f:  # Open the file in read/write binary mode
        f.seek(position[0])  # Move to the start of the position tuple
        original_data = f.read(position[1])  # Read the number of bytes specified in position tuple
        if len(original_data) != position[1]:
            raise ValueError("The specified position exceeds the file length.")

        # Replace the data only if the lengths match
        if len(new_string) == position[1]:
            f.seek(position[0])  # Go back to the starting position
            f.write(new_string.encode())  # Write new bytes (converted from string)
        else:
            raise ValueError("New string length must match the length of the original bytes being replaced.")

# Example usage:
file_path = 'example.txt'

# Create an example file if it doesn't exist
with open(file_path, 'wb') as f:
    f.write(b'thisissomethingasperfectlygood.')

# Define the position (start index, length)
position = (4, 4)  # Starting at index 4, replacing 4 bytes

# Define the new string
new_string = '01234'  # New string must be exactly 4 bytes

# Call the function to replace bytes
replace_bytes_in_file(file_path, position, new_string)

# Verify the result
with open(file_path, 'rb') as f:
    result = f.read()
    print(result.decode())
