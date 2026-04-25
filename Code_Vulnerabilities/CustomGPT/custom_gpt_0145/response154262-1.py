
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call the Manifest function and return its result
        elif string == 'Intent':
            return Intent()  # Call the Intent function and return its result
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
                # Update 'string' with the new input so the loop can handle it
                string = x

# Example implementation of Manifest and Intent functions for testing purposes
def Manifest():
    print("Manifest function called.")
    return "Manifest Completed"

def Intent():
    print("Intent function called.")
    return "Intent Completed"

# Example list of available options
andHelp = ["Intent", "Manifest"]

# Start the Help function with an initial option
Help("initial")  # You can pass any string, it will be replaced in the loop
