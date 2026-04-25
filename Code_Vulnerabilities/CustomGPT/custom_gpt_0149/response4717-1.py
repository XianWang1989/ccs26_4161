
# Open the file using a context manager for better resource handling
with open('reg.fa', 'r') as fh:
    for line in fh:
        line = line.strip()  # Remove newline characters and extra spaces
        # Process each line here
        print(line)  # Example processing (you can modify this as needed)
