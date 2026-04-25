
file_path = 'reg.fa'

# Open the file for reading
with open(file_path, 'r') as fh:
    for line in fh:  # Read the file line by line
        # Process the line here
        line = line.replace('\n', '')  # Remove newline characters, if required

        # For example, you can append the processed line to a list
        # Or perform other processing as needed
        # Here, we will just print the processed line
        print(line)
