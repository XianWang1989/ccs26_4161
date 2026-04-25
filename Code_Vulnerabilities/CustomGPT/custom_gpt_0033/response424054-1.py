
while True:  # exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')
        NumOfPpl = int(NumOfPpl)  # convert input to integer
        break  # exit the loop if num is an integer
    except ValueError:
        print("\nPlease make sure you enter a number only!\n\tand please do not leave blank!")

print("\nIs there any of these people present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for both A and B")
