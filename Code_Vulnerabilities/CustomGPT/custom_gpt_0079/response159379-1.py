
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Define your equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # Use a unique identifier for the hash

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will return False
