
def path_sel():
    while True:
        path = input("Select desired working directory: ")  # Use input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)

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
                print("This path is a directory. Please select another.")
            else:
                break  # Exit the loop if a valid file is selected

file_dl()
