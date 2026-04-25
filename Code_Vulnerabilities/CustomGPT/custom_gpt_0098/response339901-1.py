
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f'An error occurred: {e}')  # Outputs: An error occurred: division by zero
else:
    print('No exceptions occurred, result:', result)
finally:
    print('This will always execute.')
