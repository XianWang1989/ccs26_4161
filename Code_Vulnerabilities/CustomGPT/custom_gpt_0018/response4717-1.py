
# Open the file and process it line by line
with open('reg.fa', 'r') as fh:
    # Process each line one at a time
    for line in fh:
        # Remove newline characters
        line = line.rstrip('\n')
        # You can process each line as needed
        print(line)  # Replace this with whatever processing you need
