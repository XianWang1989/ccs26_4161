
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except Exception:
    e = "An error occurred"  # Custom error message or handling
    print(e)
