
import os
import stat

def check_permissions(path):
    if os.path.exists(path):
        mode = os.stat(path).st_mode
        if mode & stat.S_IRUSR and mode & stat.S_IXUSR:
            print("Directory is readable and executable by owner")
        else:
            print("Permissions issue with the directory")
    else:
        print("Directory does not exist")

check_permissions('/path/to/static/')
