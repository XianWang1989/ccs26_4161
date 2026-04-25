
# Open the file using 'with' to ensure it closes properly
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the final result
    s = ''

    # Read and process the file line by line
    for line in fh:
        # Strip whitespace and accumulate the results
        s += line.strip()

# Print the final result
print(s)
