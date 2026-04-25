
msg = input("Message? ")
# Collect every third character in a list
third_letters = [msg[i] for i in range(0, len(msg), 3)]
# Join the letters with a space and print
output = " ".join(third_letters)
print(output)
