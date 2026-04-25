
def path_sel():
    b = []
    ftp.retrlines('LIST', b.append)

    while True:
        path = raw_input("Select desired working directory: ")

        # Check if path exists in the list
        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path, '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            # Check if the directory is valid
            if 'd' in str(c[0]):
                continue  # Loop again if it’s a directory
            else:
                break  # Exit if it’s not a directory
    file_dl()
