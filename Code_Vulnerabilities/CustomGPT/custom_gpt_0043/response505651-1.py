
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue    # Skip this iteration if the condition is met

    lineToWrite += x + "\t"  # Add the current item to lineToWrite

# After the loop, lineToWrite will contain the processed items
print(lineToWrite)
