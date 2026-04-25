
while True:
    try:
        NumOfPpl = input('Enter the number of people: ')
        NumOfPpl = int(NumOfPpl)
        break  # Exit loop if successful
    except ValueError:
        print("\nPlease make sure you key in number only!")
        print("\tand please do not leave blank!")

print("\nIs there any of these persons present?")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")
