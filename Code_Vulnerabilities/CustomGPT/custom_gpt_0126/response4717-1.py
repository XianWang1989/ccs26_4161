
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the data
    s = ''
    # Read the file line by line
    for line in fh:
        # Remove the newline character and add the line to the string
        s += line.strip()  # Using strip() to remove whitespace including newlines

# Print the concatenated string
print(s)
