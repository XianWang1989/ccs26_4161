
# Improved file handling for large files
filename = 'reg.fa'

# Open the file and process it line by line
with open(filename, 'r') as fh:
    for line in fh:
        # Process the line as needed
        line = line.strip()  # Remove leading/trailing whitespace including newlines
        # Do your processing here
        print(line)  # Example of processing the line
