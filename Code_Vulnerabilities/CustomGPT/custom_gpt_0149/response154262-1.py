
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
                # Instead of calling Help recursively, just set the string
                string = x  # Update the string for the next iteration

# Example implementations for Manifest and Intent functions
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

# Sample list for demonstration
andHelp = ["Intent", "Manifest"]
