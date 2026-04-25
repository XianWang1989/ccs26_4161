
lineToWrite = ""

for x in line:
    # Check if the current company is 'XXX'
    if x == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += x + "\t"  # Append the company to lineToWrite

# Now lineToWrite will contain all companies except 'XXX'
print(lineToWrite)
