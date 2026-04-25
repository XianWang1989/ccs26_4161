
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue  # Skip this iteration if condition is met
    else:
        lineToWrite += x + "\t"  # Append the item to lineToWrite

# Optionally, print or use lineToWrite as needed
print(lineToWrite)
