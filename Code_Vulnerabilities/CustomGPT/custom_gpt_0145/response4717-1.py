
# Example code for handling large files in Python
with open('reg.fa', 'r') as fh:
    for line in fh:
        # Process each line, for example:
        line = line.strip()  # Remove whitespace from the start and end of the line
        # Do something with the processed line
        print(line)  # Or store in a list or perform other operations
