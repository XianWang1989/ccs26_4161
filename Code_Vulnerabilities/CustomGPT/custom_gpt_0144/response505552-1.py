msg = input("Message? ")
length = len(msg)
selected_chars = []

for i in range(0, length, 3):
    selected_chars.append(msg[i])

print(" ".join(selected_chars))
