
def path_sel():
    path = input("Select desired working directory: ")  # Use input for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names for comparison
    if path not in [item.split()[-1] for item in b]:  # Get the directory names
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Re-ask for input

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)
    if any('d' in item for item in c):  # Check if there are directories in the list
        return path_sel()  # Go back if it's a directory

# Call the function
path_sel()
