
try:
    result = 10 / 0
except Exception:
    e = "An error occurred."  # Here you can't directly assign from Exception
    print(e)
else:
    print("No errors! Result is:", result)
finally:
    print("This message always prints.")
