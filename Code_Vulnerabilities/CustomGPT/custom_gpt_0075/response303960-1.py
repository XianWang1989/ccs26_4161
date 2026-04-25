
# Check if pymongo can be imported successfully
try:
    import pymongo
    print("pymongo imported successfully.")
except SyntaxError as e:
    print(f"Syntax Error: {e}")
