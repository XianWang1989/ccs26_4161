
try:
    file = open('somefile.txt', 'r')
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
else:
    print("File read successfully!")
finally:
    file.close()  # This will execute no matter what
