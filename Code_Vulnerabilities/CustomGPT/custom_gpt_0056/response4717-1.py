
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the contents
    s = ''

    # Iterate through the file line by line
    for line in fh:
        # Remove newlines and append to the string
        s += line.strip()

# Now 's' contains the file contents without any newlines
print(s)
