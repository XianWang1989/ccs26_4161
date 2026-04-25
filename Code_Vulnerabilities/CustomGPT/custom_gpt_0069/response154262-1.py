
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
            x = input('What option do you choose: ').strip()
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update string to the new input

# Example definitions for Manifest and Intent
def Manifest():
    print("Manifest function is called.")

def Intent():
    print("Intent function is called.")

# Example array of help options
andHelp = ['Manifest', 'Intent']
