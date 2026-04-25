
def process_large_file(file_name):
    with open(file_name, 'r') as fh:
        s = ''
        for line in fh:
            s += line.strip()  # Remove newlines and accumulate the string
    print(s)

process_large_file('reg.fa')
