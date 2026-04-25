
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Iterate over each line in the file
    for line in fh:
        # Process each line (e.g., remove newlines and replace as needed)
        processed_line = line.strip()  # Removes leading and trailing whitespace
        # Do something with the processed line, like printing or accumulating results
        print(processed_line) # Replace this with your processing logic
