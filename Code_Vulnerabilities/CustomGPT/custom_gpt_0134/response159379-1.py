
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Or your custom equality logic here

    def __hash__(self):
        return hash(id(self))  # Or a more meaningful hash based on your class attributes

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Outputs: False
print(hash(obj1))    # Outputs a hash value
