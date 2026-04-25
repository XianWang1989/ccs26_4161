
def path_sel():
    path = input("Select desired working directory: ")  # Use input() in Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean the directory list to extract only directory names
    dirs = [line.split()[-1] for line in b if line.startswith('d')]  # Assuming 'd' indicates a directory

    if path not in dirs:
        print("ERROR- Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()

file_dl()
