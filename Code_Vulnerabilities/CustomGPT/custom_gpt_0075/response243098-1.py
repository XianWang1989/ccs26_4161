
def path_sel():
    while True:
        path = input("Select desired working directory: ")  # Use input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR- Directory does not exist.\n")
            continue  # Prompt the user again if directory does not exist
        else:
            print(f'\nChanging to {path}\n')
            ftp.cwd(path)
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)
            if any('d' in item for item in c):  # Check for subdirectories
                print("This directory has subdirectories.")
            break  # Exit the loop when a valid directory is found

    file_dl()
