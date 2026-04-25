
def path_sel():
    b = []
    ftp.retrlines('LIST', b.append)

    while True:
        path = input("Select desired working directory: ")  # Use input() for Python 3
        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                print("This is a directory.")
                continue  # Ask for path again if required
            else:
                break  # Exit the loop if a valid path is chosen

    file_dl()  # Proceed to file download

# Make sure to handle ftp connection and the rest of your code too.
