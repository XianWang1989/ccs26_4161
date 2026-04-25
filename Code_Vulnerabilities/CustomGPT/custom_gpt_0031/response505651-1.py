
lineToWrite = ""
for x in line:
    if x == 'XXX':  # Check if the current item is 'XXX'
        continue     # Skip the rest of the loop if true
    else:
        lineToWrite += x + "\t"  # Append the current item to lineToWrite
