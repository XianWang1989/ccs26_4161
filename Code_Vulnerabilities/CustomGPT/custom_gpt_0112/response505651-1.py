
lineToWrite = ""
lines = ["CompanyA", "CompanyB", "XXX", "CompanyC"]

for newCompany in lines:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output: CompanyA	CompanyB	CompanyC	
