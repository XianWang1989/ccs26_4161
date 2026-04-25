
def path_sel():
    path = input("Select desired working directory: ").strip()  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean up the directory names from the list
    directories = [item.split()[8] for item in b if item.startswith('d')]  # Assuming the directory name is in the 9th position

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in line for line in c):  # Check if there are any directories in the list
            path_sel()

# Call your downloading function here
file_dl()
