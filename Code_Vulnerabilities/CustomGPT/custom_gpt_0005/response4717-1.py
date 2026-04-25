
# Open the file using 'with' for better resource management
with open('reg.fa', 'r') as fh:
    # Process the file line by line
    for line in fh:
        line = line.strip()  # Remove leading and trailing whitespace
        print(line)  # Process the line (print, store, etc.)
