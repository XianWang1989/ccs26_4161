
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for company in line:
    if company == 'XXX':
        continue
    else:
        lineToWrite += company + "\t"

print(lineToWrite)
