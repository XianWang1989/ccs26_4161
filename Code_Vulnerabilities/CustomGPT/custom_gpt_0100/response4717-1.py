
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store processed lines
    s = ''

    # Iterate through each line in the file
    for line in fh:
        # Remove newlines and append to the string
        s += line.strip()  # strip() removes leading/trailing whitespace

# Print the resulting string
print(s)
