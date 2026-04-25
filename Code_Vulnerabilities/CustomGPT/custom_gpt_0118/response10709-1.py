
# Open the file in binary append mode
with open('example.txt', 'ab+') as file:
    # Seek to the position (4, 0)
    position = 4
    file.seek(position)

    # The new bytes to write
    new_bytes = b'01234'

    # Read the current bytes to ensure we know the length
    current_bytes = file.read(len(new_bytes))

    # Go back to the position for overwriting
    file.seek(position)

    # Write the new bytes
    file.write(new_bytes)

    # If we want to truncate the file to remove old bytes
    # (Make sure it doesn't exceed the original length)
    file.truncate()

# To read back from the file and verify
with open('example.txt', 'rb') as file:
    content = file.read()
    print(content)  # Should show: b'this01234ethingasperfectlygood.'
