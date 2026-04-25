
def path_sel():
    while True:
        path = input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Normalize input for comparison
        if path not in [entry.strip() for entry in b]:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)
            # Check if the first entry indicates a directory
            if 'd' in str(c[0]):
                print("You selected a directory.")
            else:
                print("This is not a directory.")
            break

file_dl()
