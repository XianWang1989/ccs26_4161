
# File: handle_large_file.py

def process_large_file(filename):
    with open(filename, 'r') as fh:
        s = ''
        for line in fh:
            s += line.strip()  # Strip newlines and accumulate lines

    print(s)

if __name__ == "__main__":
    process_large_file('reg.fa')
