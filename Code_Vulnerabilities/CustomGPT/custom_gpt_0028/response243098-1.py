
def path_sel():
    while True:
        path = input("Select desired working directory: ")  # Use input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            # Optionally check the directory after changes
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                print("Directory contains subdirectories.")
            break  # Exit the loop once a valid path is selected

# Call your file download function afterwards
file_dl()
