
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Define your equality condition here

    def __hash__(self):
        return hash((self.__class__,))  # Return a hash based on the class

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # Should return False
print(hash(a), hash(b))  # Hash values should be consistent
