
# Open the file in 'ab+' mode
with open('yourfile.txt', 'ab+') as file:
    # Move to the specified position (4,0) - we only need the start position
    file.seek(4)

    # Replace the bytes for the segment "issom"
    replacement_string = b'01234'  # Use bytes
    file.write(replacement_string)

    # Optionally, to make sure the rest of the file stays intact,
    # you may want to truncate the file if the new string is shorter
    file.truncate()
