
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Strip whitespace
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the listings for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()  # Check directories again
        else:
            file_dl()  # Proceed to download files
