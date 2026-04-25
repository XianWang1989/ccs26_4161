
# Open the file using a context manager to ensure it closes properly
with open('reg.fa', 'r') as fh:
    # Read and process the file line by line
    for line in fh:
        # Remove newline characters
        line = line.strip()
        # Add your processing logic here
        print(line)  # Replace with actual processing code
