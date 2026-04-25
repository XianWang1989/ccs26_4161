
while True:
    try:
        NumOfPpl = int(input('Enter the number of people: '))
        break  # Exit loop if the number is valid
    except ValueError:
        print("\nPlease make sure you enter a number and do not leave it blank!\n")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65 years old and above")
print("\tC. None for both A and B\n")
