
def method_one():
    pass

def method_two():
    pass

favorite_methods = {
    "Method One": method_one,
    "Method Two": method_two,
}

def navigate_to_method(method_name):
    method = favorite_methods.get(method_name)
    if method:
        method()  # Call or do something with the method
    else:
        print("Method not found!")

# Example usage
navigate_to_method("Method One")  # Access your method directly
