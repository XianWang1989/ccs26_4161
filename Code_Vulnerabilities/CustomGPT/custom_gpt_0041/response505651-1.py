
lineToWrite = ""
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"

print(lineToWrite)  # This will output: ABC	DEF	GHI	
