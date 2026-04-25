
try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as e:
    # Handle the exception and store it in variable e
    print("An error occurred:", e)
else:
    # This will execute if no exceptions are raised
    print("The result is:", result)
finally:
    # This block always executes, regardless of exceptions
    print("Execution complete.")
