
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue  # Skip the current iteration if 'XXX' is found

    lineToWrite += x + "\t"  # Append the company name to lineToWrite

print(lineToWrite)
