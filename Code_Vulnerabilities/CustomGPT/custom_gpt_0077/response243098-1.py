
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean the directory listing by only extracting the names
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask for a directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the newly listed content has directories
        if any(line.startswith('d') for line in c):
            path_sel()  # Re-ask for a directory

file_dl()
