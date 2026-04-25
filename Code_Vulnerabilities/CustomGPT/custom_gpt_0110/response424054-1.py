
while True:
    try:
        num_of_people = input('Enter the number of people: ')
        num_of_people = int(num_of_people)
        break
    except ValueError:
        print("\nPlease ensure you enter a number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")
