
def Help():
    while True:
        string = input("What option do you choose (Manifest, Intent, or Q to quit): ")

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            print("Quitting...") 
            break
        else:
            print('The options available are: \n')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit \n')

# Sample function definitions for Manifest and Intent
def Manifest():
    print("You chose Manifest!")

def Intent():
    print("You chose Intent!")

# Call the Help function
Help()
