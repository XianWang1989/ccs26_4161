
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue  # Skip this iteration if it matches 'XXX'

    # If the condition is not met, append to lineToWrite
    lineToWrite += x + "\t"

print(lineToWrite)  # Display the result
