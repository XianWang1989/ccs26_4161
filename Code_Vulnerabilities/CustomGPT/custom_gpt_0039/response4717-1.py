
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    result = []
    # Read the file line by line
    for line in fh:
        # Remove the newline characters and add to the result list
        result.append(line.strip())

# Join the list into a single string if needed
s = ''.join(result)
print(s)
