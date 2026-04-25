
while True:
    try:
        NumOfPpl = int(input('Enter the number of people: '))
        break  # exit loop if valid input
    except ValueError:
        print("\nPlease make sure you enter a number only and do not leave blank!")

print("\nIs there any of these persons present?")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")
