
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Check if the directory is in the list
        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                continue  # Loop back to ask for another directory if needed
            break  # Exit the loop if no further input is needed
    file_dl()
