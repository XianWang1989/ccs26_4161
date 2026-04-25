
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    result = ''

    # Iterate through the file line by line
    for line in fh:
        # Remove newline characters and add to result
        result += line.strip()

# Print the concatenated result
print(result)
