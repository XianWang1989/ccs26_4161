
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Process each line one at a time
    for line in fh:
        # Remove any newline characters
        line = line.strip()
        # Process the line (for example, print it or append it to a list)
        print(line)  # Or perform any other operation
