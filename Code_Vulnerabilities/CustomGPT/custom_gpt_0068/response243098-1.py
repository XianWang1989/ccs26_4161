
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)  # Retrieve the list of directories

    # Check if the path is in the list
    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Re-ask for input

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)  # Change working directory
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)  # Retrieve new list of directories

    # Check if the first line contains a 'd', indicating it's a directory
    if 'd' in str(c[0]):
        return path_sel()  # Re-ask for directory if needed

    return path  # Successfully selected path

# When you call path_sel(), it will return a valid path or continue to ask.
selected_path = path_sel()
file_dl()  # Proceed with downloading files
