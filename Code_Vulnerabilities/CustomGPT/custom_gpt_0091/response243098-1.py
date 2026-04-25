
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names in the list
    normalized_dirs = [line.split()[-1] for line in b]  # Assuming directory names are the last space-separated item

    if path not in normalized_dirs:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item is a directory
        if 'd' in str(c[0]):
            path_sel()

# Call the function to start
file_dl()
