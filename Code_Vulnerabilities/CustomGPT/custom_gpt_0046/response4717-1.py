
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Read line-by-line
    for line in fh:
        # Process each line (remove newline characters)
        line = line.strip()
        # Print or store the processed line
        print(line)
