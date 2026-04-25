
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the accumulated lines
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters from the line and accumulate in 's'
        s += line.strip()

# Print the final result
print(s)
