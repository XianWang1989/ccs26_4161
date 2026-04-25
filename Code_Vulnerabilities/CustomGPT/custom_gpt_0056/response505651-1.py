
lineToWrite = ""
line = ['Company A', 'Company B', 'XXX', 'Company D']

for x in line:
    if x == 'XXX':
        continue  # Skip the current iteration if x is 'XXX'

    lineToWrite += x + "\t"  # Append the company name to lineToWrite

print(lineToWrite.strip())  # Outputs: Company A	Company B	Company D
