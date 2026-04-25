
msg = input("Message? ")
length = len(msg)
output = ""

for i in range(0, length, 3):
    output += msg[i] + " "

print(output.strip())
