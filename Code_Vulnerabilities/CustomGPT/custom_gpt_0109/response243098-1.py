
def path_sel():
    path = input("Select desired working directory: ")  # Use input() in Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Debugging output
    print("Available directories:", b)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Debugging output
        print("Current directory contents:", c)

        if 'd' in str(c[0]):
            path_sel()

file_dl()
