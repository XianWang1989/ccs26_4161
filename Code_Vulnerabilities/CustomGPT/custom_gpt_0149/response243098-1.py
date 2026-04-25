
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path exists in the list of directories
    if not any(path in item for item in b):
        print("ERROR- Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Ensure you're checking the directory correctly
        if 'd' in str(c[0]):  # Adjust your check as necessary
            path_sel()

file_dl()
