
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check if the current company is 'XXX'
        continue     # Skip this iteration if true

    lineToWrite += x + "\t"  # Append to lineToWrite if condition is not met

print(lineToWrite)
