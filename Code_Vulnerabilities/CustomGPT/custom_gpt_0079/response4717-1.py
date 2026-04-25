
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Use a generator to read lines one at a time
    for line in fh:
        # Process each line (removing newline characters)
        line = line.strip()  # removes leading/trailing whitespace and newlines
        # Perform any needed operations on the line
        print(line)  # or store/append to a list if needed
