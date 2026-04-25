
try:
    file = open('example.txt', 'r')
    # Perform file operations that may raise exceptions
except Exception as e:
    print("An error occurred:", e)
finally:
    file.close()  # Always runs to ensure the file is closed safely
