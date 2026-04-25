
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        # Implement your equality logic here
        return False

    def __hash__(self):
        # Provide a hash implementation
        return id(self)  # or a specific hash computation based on attributes

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # Should print False
