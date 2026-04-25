
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
                continue  # If it's a directory, ask again
            break  # Exit loop if a valid directory is found

    file_dl()
