
msg = input("Message? ")
length = len(msg)
# Collect every third letter
third_letters = [msg[i] for i in range(0, length, 3)]
# Join with spaces and print
output = " ".join(third_letters)
print(output)
