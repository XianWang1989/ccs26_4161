
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the condition for the current item x
        continue  # Skip this iteration if the condition is met

    lineToWrite += x + "\t"  # Concatenate the item to lineToWrite
