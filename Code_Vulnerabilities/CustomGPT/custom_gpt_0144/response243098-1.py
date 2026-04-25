def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract the last word from each line (usually the name of the file/dir)
    dir_names = [line.split()[-1] for line in b]

    if path not in dir_names:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in c[0]:  # This is a bit vague, refine if needed
            path_sel()

file_dl()
