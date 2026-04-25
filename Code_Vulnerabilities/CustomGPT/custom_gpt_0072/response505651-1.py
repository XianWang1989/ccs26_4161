
line = ["ABC", "XXX", "DEF"]  # Example list
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the condition is met
    else:
        lineToWrite += newCompany + "\t"  # Append to lineToWrite

print(lineToWrite.strip())  # Print result without trailing tab
