
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path is in the directory list
    if path not in [line.split()[-1] for line in b]:  # Extract directory names correctly
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if it's a directory by looking for 'd'
        if any('d' in line for line in c):  # Check if any line indicates a directory
            path_sel()
        else:
            file_dl()

# Make sure to call the function to run it
path_sel()
