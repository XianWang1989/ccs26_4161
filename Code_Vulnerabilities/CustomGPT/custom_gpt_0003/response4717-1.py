
# Efficient file handling for large files
filename = 'reg.fa'  # Replace this with your large file's path
lines = []

# Open the file using a context manager
with open(filename, 'r') as fh:
    for line in fh:
        # Process each line as required
        # Here I'm just appending to a list, but you can perform any operations
        lines.append(line.strip())  # .strip() removes leading/trailing whitespace including newlines

# If needed, do something with lines after processing
# For demonstration, we will print the first 10 processed lines
print(lines[:10])
