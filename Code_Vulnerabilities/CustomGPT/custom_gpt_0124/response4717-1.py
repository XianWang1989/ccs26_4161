
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the output
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove the newline character and add to the string
        s += line.strip()  # strip() removes whitespace including newlines

# Print the final result
print(s)
