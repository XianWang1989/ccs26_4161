
msg = input("Message? ")
# Select every third letter
third_letters = [msg[i] for i in range(0, len(msg), 3)]
# Join the letters with a space and print the result
output = " ".join(third_letters)
print(output)
