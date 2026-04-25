
try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except Exception as e:  # Catching the exception
    print("An error occurred:", e)
else:
    print("No exceptions occurred, and the result was calculated successfully.")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
