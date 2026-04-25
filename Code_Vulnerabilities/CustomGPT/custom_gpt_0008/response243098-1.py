
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Ensure paths in b are stripped of newline characters and spaces
    b = [line.strip() for line in b]

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Recursive call to ask for directory again
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Ensure to check if the first line has a directory indicator
        if 'd' in str(c[0]):
            path_sel()  # Recursive call if it's a directory

# Call the function
file_dl()
