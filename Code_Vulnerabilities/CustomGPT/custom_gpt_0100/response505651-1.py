
lineToWrite = ""

# Assuming `line` is a list containing company names
for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    # This will execute for all companies except 'XXX'
    lineToWrite += newCompany + "\t"

print(lineToWrite)
