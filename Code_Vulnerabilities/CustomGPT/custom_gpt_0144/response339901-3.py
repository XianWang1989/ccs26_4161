try:
    print("Trying something risky...")
    result = 10 / 0
except Exception as e:
    print("Handled exception:", e)
else:
    print("No exceptions occurred!")
finally:
    print("This always runs.")
