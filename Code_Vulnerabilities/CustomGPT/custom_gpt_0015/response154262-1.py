
def Help():
    while True:
        string = input("What option do you choose (Manifest/Intent) or type Q to Quit: ")
        print('\n')

        if string == 'Manifest':
            return Manifest()  # Call your Manifest function
        elif string == 'Intent':
            return Intent()  # Call your Intent function
        elif string == 'Q':
            break
        else:
            print('The options available are:')
            for i in andHelp:
                print(i)

# Example functions to demonstrate the behavior
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

# Example list for andHelp
andHelp = ['Manifest', 'Intent']

# Call the Help function
Help()
