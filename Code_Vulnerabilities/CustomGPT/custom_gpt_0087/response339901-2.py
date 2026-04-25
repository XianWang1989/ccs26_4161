
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("This will always execute.")
