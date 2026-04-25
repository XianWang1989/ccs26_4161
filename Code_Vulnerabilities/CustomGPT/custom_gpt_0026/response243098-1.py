
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract just the directory names from the listing
    directory_names = [line.split()[-1] for line in b]

    if path not in directory_names:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Recursively ask for input again
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory
        if 'd' in str(c[0]):
            path_sel()  # If it's a directory, ask for input again

file_dl()
