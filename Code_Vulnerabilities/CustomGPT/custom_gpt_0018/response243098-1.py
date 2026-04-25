
def path_sel():
    while True:  # Infinite loop until a valid path is entered
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)
        if path not in b:
            print("ERROR- Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                continue  # Re-ask for a new path if the current one is a directory
            break  # Exit the loop if a valid directory is selected

    file_dl()
