
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue  # Skip this iteration if Company is 'XXX'

    lineToWrite += x + "\t"  # Append to lineToWrite if condition is not met

print(lineToWrite)  # Output the result
