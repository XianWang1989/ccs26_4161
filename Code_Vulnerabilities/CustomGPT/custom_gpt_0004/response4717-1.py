
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Read the file line by line
    for line in fh:
        # Process each line (removing newline characters)
        line = line.strip()
        # Here you can do whatever processing you need with 'line'
        print(line)  # Example of printing processed lines
