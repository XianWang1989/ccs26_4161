
def check_indentation(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if '\t' in line and ' ' in line:
                print("Mixed indentation found!")
                break
        else:
            print("No mixed indentation.")

check_indentation('your_script.py')
