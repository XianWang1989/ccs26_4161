
# Open the file using a context manager to ensure proper closing
with open('reg.fa', 'r') as fh:
    # Process the file line by line
    for line in fh:
        # Remove newline characters
        line = line.strip()  
        # Do whatever processing you need with the line
        print(line)  # Replace this with your actual processing
