
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Check if the path exists in the retrieved list
        if path not in b:
            print("ERROR - Directory does not exist. Please try again.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)
            # Check if the first item indicates a directory
            if 'd' in str(c[0]):
                continue  # Re-ask for directory if the first entry is a directory
            break  # Exit the loop if a valid directory is selected

file_dl()
