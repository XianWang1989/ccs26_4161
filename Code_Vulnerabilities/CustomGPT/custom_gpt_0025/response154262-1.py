
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
                return  # Exit the function by returning
            else:
                Help(x)  # Call Help without needing to break

# Example of supporting function definitions
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Dummy options for demonstration
andHelp = ['Manifest', 'Intent']
