
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
                string = x  # Update string for the next iteration

# Example implementations for Manifest and Intent
def Manifest():
    print("Manifest function called.")
    return

def Intent():
    print("Intent function called.")
    return

# Example list for andHelp
andHelp = ['Manifest', 'Intent']
