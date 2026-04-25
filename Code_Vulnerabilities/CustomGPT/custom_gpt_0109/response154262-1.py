
def Help():
    while True:
        string = input('What option do you choose (Manifest, Intent, or Q to Quit): ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            print('Exiting...')
            break
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit \n')

# Example of the Manifest and Intent functions (for completeness)
def Manifest():
    print("Manifest function executed!")

def Intent():
    print("Intent function executed!")

andHelp = ['Manifest', 'Intent']  # Example options
Help()
