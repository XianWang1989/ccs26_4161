
def Help():
    while True:
        string = input("What option do you choose (Manifest/Intent/Q to Quit): ")

        if string == 'Manifest':
            return Manifest()  # Call your Manifest function here
        elif string == 'Intent':
            return Intent()  # Call your Intent function here
        elif string == 'Q':
            print("Quitting...")
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

andHelp = ['Intent', 'Manifest']  # Example options
Help()  # Starts the help function
