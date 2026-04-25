
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract just the directory names
    dir_list = []
    for line in b:
        parts = line.split()
        if parts and parts[0][0] == 'd':  # Check if it's a directory (starts with 'd')
            dir_list.append(parts[-1])  # Assuming the last part is the directory name

    if path not in dir_list:
        print "ERROR- Directory does not exist.\n"
        path_sel()
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):
            path_sel()

file_dl()
