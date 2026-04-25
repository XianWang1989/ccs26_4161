
# Let's assume your file is named 'example.txt'
filename = 'example.txt'

# Original content (for reference) - this would exist in the file
# "thisissomethingasperfectlygood."
original_string = b"thisissomethingasperfectlygood."

# The string to replace the bytes with
replacement_string = b"01234"

# The position to start replacing (4, 0) -> means start at byte position 4
start_position = 4
length_to_replace = len(replacement_string)

# Open the file in 'ab+' mode
with open(filename, 'ab+') as file:
    # Move the pointer to the start position
    file.seek(start_position)

    # Read existing content after the position to ensure we don't overwrite important part
    remaining_content = file.read()

    # Move the pointer back to the same position to write new content
    file.seek(start_position)

    # Write the new content
    file.write(replacement_string)

    # If you want to maintain the file's initial structure, you may need to write back the
    # remaining content, if you intend to keep the length constant
    # For example, if the replacement string is shorter than the original length
    if length_to_replace < len(remaining_content):
        file.write(remaining_content[length_to_replace:])
