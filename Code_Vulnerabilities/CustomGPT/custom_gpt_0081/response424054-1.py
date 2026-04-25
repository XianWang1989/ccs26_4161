
while True:  # exception loop
    try:
        NumOfPpl = raw_input('Enter the number of people: ')
        NumOfPpl = int(NumOfPpl)
        break  # exit the loop if num is an integer
    except ValueError:
        print ("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print ("\nIs there any of these person present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for both A. and B. \n")
