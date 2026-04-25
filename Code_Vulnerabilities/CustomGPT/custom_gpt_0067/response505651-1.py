
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check if the current company is 'XXX'
        continue     # Skip this iteration if it is

    lineToWrite += x + "\t"  # Otherwise, add to lineToWrite

print(lineToWrite)
