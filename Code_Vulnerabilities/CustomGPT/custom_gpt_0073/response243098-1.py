
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the paths retrieved, assuming they start with 'd' for directories
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):
            path_sel()

file_dl()
