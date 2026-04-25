
def path_sel():
    path = input("Select desired working directory: ").strip()  # Use .strip() to remove any extra whitespace
    b = []
    ftp.retrlines('LIST', b.append)

    # Strip any whitespace from the listed directories
    b = [item.split()[-1] for item in b]  # assuming directory names are in the last column

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        c = [item.split()[-1] for item in c]  # process the output similarly

        if 'd' in str(c[0]):  # Consider refining this check to suit your needs
            path_sel()

file_dl()
