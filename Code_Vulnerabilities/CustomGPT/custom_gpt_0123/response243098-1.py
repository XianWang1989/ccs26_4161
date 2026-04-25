
def path_sel():
    while True:  # Use a loop to keep asking until a valid directory is found
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR - Directory does not exist.\n")
        else:
            print('\nChanging to ' + path + '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            if 'd' in str(c[0]):
                print("This is a directory, re-selecting...")
                continue  # Go back to asking for the directory
            break  # Exit the loop when a valid directory is chosen
    file_dl()
