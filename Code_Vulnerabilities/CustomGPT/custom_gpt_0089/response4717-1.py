
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Process the file line by line
    for line in fh:
        # Remove any new line characters
        line = line.strip()
        # Print or process the line as needed
        print(line)
