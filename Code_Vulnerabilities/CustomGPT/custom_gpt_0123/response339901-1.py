
try:
    # Some risky code
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception:
    e = sys.exc_info()[1]  # e now holds the caught exception (requires importing sys)
    print(e)
