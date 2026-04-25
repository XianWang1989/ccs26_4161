
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Strip whitespace and ensure consistent casing for comparison
    b = [entry.strip() for entry in b]

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask for the directory
    else:
        print('\nChanging to '+ path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for the directory if it's a directory

file_dl()
