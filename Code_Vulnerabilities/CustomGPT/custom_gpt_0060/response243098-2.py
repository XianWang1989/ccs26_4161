
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Extract directory names from the listing
        directories = [line.split()[-1] for line in b if line.startswith('d')]

        if path not in directories:
            print("ERROR- Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            # Optionally you check for directories again if needed
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                continue  # To allow re-selection of directories
            break  # Exit the loop if the directory is valid

file_dl()
