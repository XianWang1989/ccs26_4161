
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in [entry.split()[-1] for entry in b]:  # Only check directory names
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-prompt user
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if any(entry.startswith('d') for entry in c):  # Check if there are directories in the listing
            path_sel()  # Re-prompt if there's a directory

file_dl()
