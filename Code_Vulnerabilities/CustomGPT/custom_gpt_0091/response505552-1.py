
msg = input("Message? ")
# Get every third letter
result = [msg[i] for i in range(0, len(msg), 3)]
# Join the letters with a space and print
output = " ".join(result)
print(output)
