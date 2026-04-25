lines = ["Apple", "XXX", "Google", "XXX", "Microsoft"]
lineToWrite = ""

for newCompany in lines:
    if newCompany == "XXX":
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)
