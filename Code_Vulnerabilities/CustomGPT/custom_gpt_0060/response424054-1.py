
while True:  # exceptional loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # for Python 3.x, use input(), for Python 2.x, use raw_input()
        NumOfPpl = int(NumOfPpl)  # Trying to convert input to an integer
        break  # exit the loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only!")
        print("\tand please do not leave blank!")

# Remaining question after valid input is received
print("\nIs there any of these person present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")
