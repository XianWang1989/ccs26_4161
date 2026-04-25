
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
                string = x  # update `string` to the new input

# Example of the Manifest and Intent functions
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

# Example options
andHelp = ['Intent', 'Manifest']
