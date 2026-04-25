
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3.x
    b = []
    ftp.retrlines('LIST', b.append)  # Retrieve the list of directories

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)  # Change to the selected directory
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)  # Retrieve the list of directories again

        if 'd' in str(c[0]):  # Check if the first item in the list indicates a directory
            return path_sel()  # Allow to select another directory if needed

    return path  # Return the valid path at the end
