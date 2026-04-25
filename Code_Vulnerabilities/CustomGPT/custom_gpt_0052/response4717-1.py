
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''
    # Iterate through each line in the file
    for line in fh:
        # Remove newline characters and update string
        s += line.strip()

# Print the final result
print(s)
