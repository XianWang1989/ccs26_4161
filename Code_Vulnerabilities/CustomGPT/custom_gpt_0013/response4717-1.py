
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the processed content
    result = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and process the line as needed
        result += line.strip()  # Use strip() to remove leading/trailing whitespace

# Now you can use the result as needed
print(result)
