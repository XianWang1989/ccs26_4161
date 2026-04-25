
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the list for easier matching
    directories = [entry.split()[-1] for entry in b if entry.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the current path is a directory
        if 'd' in str(c[0]):  # This may need improvement based on your requirements
            path_sel()  # re-ask for directory

    file_dl()

