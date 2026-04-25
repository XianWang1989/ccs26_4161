
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Implement your equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # Use the id of the instance for hashing

# Example usage
a = MyClass()
b = MyClass()
print(a == b)  # This should not raise a warning and will print False
