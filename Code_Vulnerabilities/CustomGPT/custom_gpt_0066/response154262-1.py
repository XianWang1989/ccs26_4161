
def Help():
    while True:
        string = input("What option do you choose (Manifest/Intent/Q): ")

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example of the functions that might be called
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

# Example available help options
andHelp = ["Manifest", "Intent"]
