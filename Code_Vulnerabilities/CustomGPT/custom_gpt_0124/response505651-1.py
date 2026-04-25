
line = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite.strip())  # Output: ABC    DEF    GHI
