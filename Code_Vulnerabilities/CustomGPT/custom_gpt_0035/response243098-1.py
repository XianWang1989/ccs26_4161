
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean the directory listings for accurate comparison
    dir_list = [line.split()[-1] for line in b]  # Assuming last element is the directory name

    if path not in dir_list:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list indicates a directory
        if 'd' in str(c[0]):
            path_sel()

file_dl()
