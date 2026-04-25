
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the content
    s = ''

    # Iterate through the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()

# Print the result after processing
print(s)
