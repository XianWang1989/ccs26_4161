
msg = input("Message? ")
# Using list comprehension to get every third letter
third_letters = [msg[i] for i in range(0, len(msg), 3)]
# Joining the letters with a space
result = " ".join(third_letters)
print(result)
