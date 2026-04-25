
def path_sel():
    while True:
        path = input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)
        directories = [entry.split()[-1] for entry in b if entry.startswith('d')]

        if path not in directories:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path, '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            if 'd' in str(c[0]):
                continue  # Re-ask for directory if still a directory
            break  # Exit loop when a valid non-directory is selected

    file_dl()
