
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path is in the list of directories
    if path not in b:
        print "ERROR- Directory does not exist.\n"
        return path_sel()  # Return the result of the recursive call
    else:
        print '\nChanging to '+ path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item contains 'd', indicating a directory
        if 'd' in str(c[0]):
            print "This is a directory. Please enter a different path."
            return path_sel()  # Return the result of the recursive call

    return path  # Return the valid path when found

# Then you can call the function and capture the result:
selected_path = path_sel()
file_dl(selected_path)
