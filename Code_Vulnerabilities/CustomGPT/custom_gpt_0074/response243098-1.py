
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Clean 'b' to only retain directory names
        directory_list = [line.split()[-1] for line in b]

        if path not in directory_list:
            print("ERROR- Directory does not exist.\n")
        else:
            print('\nChanging to ' + path, '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                continue  # This will re-prompt the user if 'd' is found
            break  # Exit the loop if everything is fine

file_dl()
