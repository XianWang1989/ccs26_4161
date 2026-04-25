
def path_sel():
    while True:  # Create a loop to continue prompting until a valid directory is selected
        path = input("Select desired working directory: ")  # Use input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)  # Retrieve the directory list into b

        if path not in b:
            print("ERROR- Directory does not exist.\n")
            continue  # Continue the loop if path is not valid
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)  # Change to the specified path
            print(path)
            c = []
            ftp.retrlines('LIST', c.append)  # Retrieve the directory contents into c
            if 'd' in str(c[0]):
                continue  # If the path is a directory, continue prompting for input
            else:
                break  # If a valid directory is selected, break out of the loop

    file_dl()  # Call the file download function after the directory selection is done
