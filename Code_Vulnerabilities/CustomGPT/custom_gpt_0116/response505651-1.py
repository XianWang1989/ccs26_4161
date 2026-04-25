
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue  # Skip the rest of the loop for this iteration
    else:
        lineToWrite += x + "\t"  # Add the current item to lineToWrite

print(lineToWrite)
