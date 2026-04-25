
# Open the file using 'with' to ensure proper closure
with open('reg.fa', 'r') as fh:
    # Use a generator expression to read line by line
    lines = (line.strip() for line in fh)  # This will strip whitespace including new lines

    # Loop through the lines
    for line in lines:
        # Process each line without storing all lines in memory
        print(line)  # Replace this with your processing for each line
