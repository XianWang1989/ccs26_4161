
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if path is in the list of directories
    if path not in [line.split()[-1] for line in b]:  # Split and get the last part (directory name)
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print("Current directory:", path)

        # Check for subdirectories
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check if any line indicates a directory
            print("Subdirectories found.")
            path_sel()  # You can handle this differently based on your needs

file_dl()
