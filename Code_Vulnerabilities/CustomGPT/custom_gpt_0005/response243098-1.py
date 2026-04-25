
def path_sel():
    while True:
        path = input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Normalize directory listing format
        directories = [line.split()[-1] for line in b if line.startswith('d')]

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
                continue  # Prompt for directory again if it's a directory
            break  # Exit loop if not a directory
    file_dl()
