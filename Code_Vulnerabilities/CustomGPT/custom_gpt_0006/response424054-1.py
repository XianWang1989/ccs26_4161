
while True:
    try:
        NumOfPpl = int(input('Enter the number of people: '))
        break
    except ValueError:
        print("\nPlease make sure you enter a number and do not leave it blank!")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A and B")
