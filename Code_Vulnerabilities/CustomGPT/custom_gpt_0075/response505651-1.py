
line = ['AAA', 'BBB', 'XXX', 'CCC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Append to lineToWrite

print(lineToWrite)  # Output: "AAA\tBBB\tCCC\t"
