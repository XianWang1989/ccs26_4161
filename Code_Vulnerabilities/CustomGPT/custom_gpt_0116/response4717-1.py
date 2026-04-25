
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Process each line individually
    for line in fh:
        # Strip newline characters and process the line
        processed_line = line.strip()  # Removes leading/trailing whitespace
        # You can add your processing logic here
        print(processed_line)  # Example: print the processed line
