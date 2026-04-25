
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue  # Skip this iteration if it matches 'XXX'
    else:
        lineToWrite += x + "\t"  # Add x to lineToWrite if it doesn't match

print(lineToWrite)  # Print the result to verify
