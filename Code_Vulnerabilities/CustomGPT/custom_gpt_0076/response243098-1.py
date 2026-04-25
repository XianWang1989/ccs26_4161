
def path_sel():
    path = input("Select desired working directory: ")  # Changed raw_input to input (Python 3)
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the paths in the list, removing leading spaces
    b = [line.split()[-1] for line in b]  # Get the last item from each line which usually represents the directory names

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)  # Change working directory
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first line contains a directory (starts with 'd')
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for input
    file_dl()  # Call file download function
