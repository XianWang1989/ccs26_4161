
while True:  # Infinite loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use input() instead of raw_input() in Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit the loop if valid number
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65 years old and above")
print("\tC. None for both A and B\n")
