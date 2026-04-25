
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the processed lines
    s = ''

    # Process each line in the file one by one
    for line in fh:
        # Remove any newline characters from the line
        s += line.strip()  # Use strip() to remove whitespace and newlines

# Print the final result
print(s)
