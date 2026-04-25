
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names for comparison
    b = [item.split()[-1] for item in b]  # Extract only directory names

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input if directory doesn't exist
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in c is a directory (assuming proper LIST output)
        if 'd' in str(c[0]):
            path_sel()  # Re-ask if the path is still a directory

file_dl()
