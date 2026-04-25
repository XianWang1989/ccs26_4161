
while True:  # Exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use input() for Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit if num is an integer
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A and B")
