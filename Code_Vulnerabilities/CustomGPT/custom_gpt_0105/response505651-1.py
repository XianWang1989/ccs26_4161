
lineToWrite = ""

# Sample list of companies
line = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration

    lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output will be: ABC     DEF     GHI
