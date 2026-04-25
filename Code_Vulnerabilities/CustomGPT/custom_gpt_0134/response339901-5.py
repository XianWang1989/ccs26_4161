
try:
    # Potentially problematic code
    f = open('file.txt', 'r')
    content = f.read()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully!")
finally:
    f.close()  # This will execute no matter what
