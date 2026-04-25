
# Open the file
with open('reg.fa', 'r') as fh:
    s = ''

    # Iterate through each line in the file
    for line in fh:
        # Remove the newline character and append to the string
        s += line.strip()

# Print the final string
print(s)
