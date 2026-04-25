
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Process the file line by line
    for line in fh:
        # Remove the newline character and perform any processing you need
        processed_line = line.strip()  # This will remove leading/trailing whitespace including the newline
        # You can add your processing logic here
        print(processed_line)  # Example action: print the processed line
