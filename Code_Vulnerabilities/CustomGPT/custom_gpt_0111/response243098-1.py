
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]  # Filter for directories

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for the directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')

        # Check if path is still a directory
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for a valid directory if needed

file_dl()
