
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters and append to string
        s += line.strip()  # strip() to remove any whitespace/newline characters

# Print the final result
print(s)
