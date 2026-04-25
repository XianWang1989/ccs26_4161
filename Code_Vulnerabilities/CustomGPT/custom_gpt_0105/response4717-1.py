
# Efficient file handling for large files in Python
filename = 'reg.fa'

with open(filename, 'r') as fh:
    # Use a generator to read file line by line
    for line in fh:
        # Process each line (for example, stripping newlines)
        line = line.strip()  # Remove any leading/trailing whitespace
        # Do something with the processed line
        print(line)

# Optionally, if you want to accumulate the results
results = []
with open(filename, 'r') as fh:
    for line in fh:
        line = line.strip()  # Remove newline characters
        results.append(line)  # Store the line for later use

# Now, results contains all the processed lines
print(results)
