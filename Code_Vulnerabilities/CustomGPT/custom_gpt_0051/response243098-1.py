
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in [line.split()[-1] for line in b]:  # Check the last element of each line for the directory name
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        # Check if 'd' is in the first line of the listing
        if 'd' in str(c[0]):
            path_sel()
        else:
            print("No subdirectories found. Ending selection.")

# Call the function to start
path_sel()
