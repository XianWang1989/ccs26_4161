
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)  # List of directories and files in current FTP location

    # Check if the input directory is present in the directory list
    directory_exists = any(path in line for line in b if line.startswith('d'))

    if not directory_exists:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Ask for a new directory until a valid one is given
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry in the list is a directory
        if any('d' in line for line in c):
            return path_sel()  # Re-ask for the directory if there's a subdirectory

    file_dl()
