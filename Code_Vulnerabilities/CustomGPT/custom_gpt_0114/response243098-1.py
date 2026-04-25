
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Check if path exists in the directory list
        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            # Check if the first entry is a directory
            if 'd' in str(c[0]):
                print("Directory confirmed.")
                # Exit loop if the path is valid
                break
            else:
                print("ERROR - First entry is not a directory, please try again.\n")

file_dl()
