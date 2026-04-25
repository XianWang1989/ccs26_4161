
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Ensure directories in `b` are accurately stored for comparison
    directories = [line.split(None, 8)[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')  # Refresh the listing after changing directory
        c = []
        ftp.retrlines('LIST', c.append)
        # Check if the current path is a directory
        if len(c) > 0 and 'd' in str(c[0]):  # Check if the first entry is a directory
            path_sel()

file_dl()
