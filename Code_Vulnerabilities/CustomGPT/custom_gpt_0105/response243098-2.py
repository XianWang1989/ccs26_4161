
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
            c = []
            ftp.retrlines('LIST', c.append)

            if any('d' in line for line in c):
                continue  # Loop back to re-ask for a directory
            else:
                break  # Exit loop if valid directory

file_dl()
