
lineToWrite = ""
line = ["CompanyA", "XXX", "CompanyB", "CompanyC"]

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)  # This will output: CompanyA	CompanyB	CompanyC
