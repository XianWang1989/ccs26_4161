
for x in line:
    if x == 'XXX':  # Check the current item in the loop
        continue  # Skip this iteration if the condition is met

    # This line executes only if the condition is not met
    lineToWrite += x + "\t"  # Append the current item to lineToWrite
