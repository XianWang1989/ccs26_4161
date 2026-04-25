
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        # Ensure 'other' is an instance of MyClass for comparison
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Your logic for equality

    def __hash__(self):
        # Return a constant hash value
        return 42  # Or implement a meaningful hash value based on instance attributes

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # Output: False
print(hash(a))  # Output: 42
