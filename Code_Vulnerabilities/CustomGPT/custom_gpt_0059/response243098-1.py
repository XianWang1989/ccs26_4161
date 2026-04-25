
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory listing for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    # Check if the path exists in the directory list
    if path not in directories:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Recursively re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)

    # Check if the current directory is a directory
    c = []
    ftp.retrlines('LIST', c.append)
    if any('d' in line for line in c):
        return path_sel()  # Re-ask if current directory is valid

    file_dl()  # Proceed to download files

