
def path_sel():
    while True:  # Keep asking until a valid directory is found
        path = raw_input("Select desired working directory: ")  # Replace with input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR- Directory does not exist.\n")
            continue  # Re-ask for the directory
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            if 'd' in str(c[0]):
                continue  # Re-ask for a new directory if the first item is a directory
            break  # Exit the loop if a valid directory was selected

    file_dl()  # Call the file download function after selection
