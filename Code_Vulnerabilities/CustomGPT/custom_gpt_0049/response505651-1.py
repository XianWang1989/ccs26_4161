
lineToWrite = ""
for x in line:
    if x == 'XXX':
        continue  # This skips the current iteration if x is 'XXX'
    else:
        lineToWrite += x + "\t"  # Concatenates to the lineToWrite variable

print(lineToWrite)
