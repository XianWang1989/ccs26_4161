
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {str(e)}")  # 'str(e)' gives the string representation of the exception
