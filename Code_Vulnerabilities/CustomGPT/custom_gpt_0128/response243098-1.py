
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Strip whitespace and get only directory names
    directories = [entry.split()[-1] for entry in b]

    if path not in directories:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Recurse to ask again
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()  # Call again if the condition is met

file_dl()
