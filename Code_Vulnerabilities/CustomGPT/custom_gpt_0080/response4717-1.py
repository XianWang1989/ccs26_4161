
def process_large_file(filename):
    with open(filename, 'r') as fh:
        s = ''
        for line in fh:
            s += line.strip()  # Use strip to remove newline characters
    print(s)

process_large_file('reg.fa')
