
def Help():
    while True:
        string = input('What option do you choose (Manifest/Intent/Q to Quit): ')
        print('\n')

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

# You would also need to define the functions Manifest(), Intent(), and the list `andHelp`
def Manifest():
    return "Manifest function called"

def Intent():
    return "Intent function called"

andHelp = ["Manifest", "Intent"]

Help()
