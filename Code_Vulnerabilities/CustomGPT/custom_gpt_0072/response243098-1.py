
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names
    directories = [line.split()[-1] for line in b]  # Get only the last part (directory name)

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if 'd' is in the first line of the directory listing
        if 'd' in str(c[0]):
            path_sel()

    file_dl()
