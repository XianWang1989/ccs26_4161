
lineToWrite = ""

# Example list of companies
lines = ['ABC', 'XXX', 'DEF', 'XYZ']

for newCompany in lines:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    # If the condition is not met, add to lineToWrite
    lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output will be: "ABC	DEF	XYZ	"
