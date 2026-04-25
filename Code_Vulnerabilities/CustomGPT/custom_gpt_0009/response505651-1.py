
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check if the current item is 'XXX'
        continue  # Skip this iteration if it is

    lineToWrite += x + "\t"  # Concatenate the current item to lineToWrite

print(lineToWrite)
