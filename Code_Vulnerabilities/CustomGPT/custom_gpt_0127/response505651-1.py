
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue  # Skip this iteration if x is 'XXX'

    lineToWrite += x + "\t"  # Add the current x to lineToWrite

print(lineToWrite)
