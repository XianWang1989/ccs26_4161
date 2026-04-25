
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Create an empty list to store processed lines
    processed_lines = []

    # Iterate over each line in the file
    for line in fh:
        # Strip newline characters and any leading/trailing whitespace
        processed_line = line.strip()

        # You can do additional processing here if needed

        # Append the processed line to the list
        processed_lines.append(processed_line)

# Join the lines back together for output, if necessary
result = '\n'.join(processed_lines)

# Print the final result
print(result)
