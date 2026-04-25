
while True:  # loop for input validation
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use `input()` instead of `raw_input()` for Python 3
        NumOfPpl = int(NumOfPpl)  # convert input to integer
        break  # exit loop if valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: ")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A and B.")
