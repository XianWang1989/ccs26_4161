
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)

            if 'd' in str(c[0]):
                print("Subdirectory exists. Please select again.")
            else:
                break  # Exit loop if directory is valid

    file_dl()
