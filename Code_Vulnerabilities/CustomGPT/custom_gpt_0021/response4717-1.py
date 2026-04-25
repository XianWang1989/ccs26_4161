
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for accumulating lines
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters and accumulate
        s += line.strip()  # .strip() removes leading/trailing whitespace

# Print the final accumulated string
print(s)
