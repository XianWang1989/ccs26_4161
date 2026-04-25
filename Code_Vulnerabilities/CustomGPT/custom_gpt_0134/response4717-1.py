
# Improved file handling for large files
with open('reg.fa', 'r') as fh:
    # Use a list to collect lines
    processed_lines = []

    # Read file line by line
    for line in fh:
        # Strip newline characters and other processing
        processed_lines.append(line.strip())

# Join processed lines into a single string if needed
result = ''.join(processed_lines)
print(result)
