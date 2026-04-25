
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract directory names from the LIST output
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR- Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)

        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list contains 'd' (indicating a directory)
        if 'd' in str(c[0]):
            path_sel()

    file_dl()
