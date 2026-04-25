
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Read the file line by line
    for line in fh:
        # Process each line (remove newline characters, etc.)
        processed_line = line.strip()  # Strips leading/trailing whitespace
        # Here you can do something with each processed_line
        print(processed_line)  # For demonstration, printing processed line
