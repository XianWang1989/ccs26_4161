
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue  # Skip this iteration if x is 'XXX'

    lineToWrite += x + "\t"

print(lineToWrite)
