
def Help():
    while True:
        x = input('What option do you choose: ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call your Manifest function here
        elif x == 'Intent':
            return Intent()     # Call your Intent function here
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for option in ['Intent', 'Manifest']:  # Update this list as needed
                print(option)
            print('Type Q to Quit \n')

# Example functions to illustrate the usage
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

# Call the Help function to start
Help()
