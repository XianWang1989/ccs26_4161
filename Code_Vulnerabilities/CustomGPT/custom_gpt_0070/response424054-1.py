
while True:  # exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use input for Python 3
        NumOfPpl = int(NumOfPpl)
        break  # exit loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only!\n\tand please do not leave blank!")

print("\nIs there any of these person present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")
