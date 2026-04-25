
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean and standardize entries in b for comparison
    directories = [entry.split()[-1] for entry in b]  

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if there's a directory in the first entry
        if 'd' in str(c[0]):
            path_sel()

file_dl()
