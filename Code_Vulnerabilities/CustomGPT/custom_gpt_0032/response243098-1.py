
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Remove leading/trailing spaces
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the listing for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()  # Re-ask if 'd' is in the listing
    file_dl()  # Assuming you have a function to handle file download

