
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("This block always executes.")
