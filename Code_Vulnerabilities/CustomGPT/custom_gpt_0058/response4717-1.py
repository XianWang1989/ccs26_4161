
# Open the file using 'with' to ensure it gets closed automatically
with open('reg.fa', 'r') as fh:
    for line in fh:
        # Process each line here
        line = line.strip()  # Remove newline characters and any leading/trailing whitespace
        # Here you can add your processing logic, for example, print the line
        print(line)
