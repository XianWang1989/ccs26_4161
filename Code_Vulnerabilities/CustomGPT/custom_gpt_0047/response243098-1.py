
def path_sel():
    while True:
        path = input("Select desired working directory: ")
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
                print("It looks like this is a directory.")
                continue  # If it's a directory, re-prompts the user

            break  # Exit the loop if it's a valid path and not a directory

file_dl()
