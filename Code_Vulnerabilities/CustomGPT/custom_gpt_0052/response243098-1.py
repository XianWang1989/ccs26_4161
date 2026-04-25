
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize paths for comparison
    b = [item.split()[-1] for item in b]  # Assuming the last item is the directory name

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list represents a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for directory if it’s a directory

file_dl()
