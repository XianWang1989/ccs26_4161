
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Strip whitespace and split items for comparison
    dir_list = [item.strip() for item in b]

    if path not in dir_list:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask user if directory doesn't exist
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)

        # Recheck after changing directory
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()  # Loop if it’s still a directory

file_dl()
