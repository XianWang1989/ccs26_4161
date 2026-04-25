
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)  # Get list of directories

    # Strip leading/trailing whitespace from each directory listing
    directories = [line.split()[-1] for line in b]

    if path not in directories:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first line indicates it's a directory
        if 'd' in str(c[0]):
            path_sel()  # Recursively ask for a new directory

file_dl()
