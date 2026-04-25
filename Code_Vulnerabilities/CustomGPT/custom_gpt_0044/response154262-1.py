
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the input to the new string value

# Sample function definitions for Manifest and Intent
def Manifest():
    print("You chose Manifest.")
    return

def Intent():
    print("You chose Intent.")
    return

# Example options
andHelp = ['Intent', 'Manifest']
Help(input("What option do you choose: "))  # Initial input to start the function
