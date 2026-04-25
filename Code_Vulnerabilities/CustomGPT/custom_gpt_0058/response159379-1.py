
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Adjust your equality condition accordingly
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # Or implement a more meaningful hash, depending on your needs

# Example usage:
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Outputs: False
print(hash(obj1))  # Outputs the hash of obj1
