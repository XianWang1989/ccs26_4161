
try:
    # code that may raise an exception
    f = open('somefile.txt', 'r')
    data = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("File read successfully.")
finally:
    f.close()  # This will run regardless of whether an exception occurred
    print("File has been closed.")
