
def path_sel():
    path = raw_input("Select desired working directory: ").strip()
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize entries in 'b' for comparison
    b = [entry.split()[-1] for entry in b]  # Assuming last part is the directory name

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory
        if 'd' in str(c[0]):
            path_sel()

file_dl()
