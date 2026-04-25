
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Or implement your actual equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # Or you can return a hash based on your attributes

# Example usage
obj1 = MyClass()
obj2 = MyClass()

# Equality check
print(obj1 == obj2)  # Should return False
print(hash(obj1))    # Provides a hash value for obj1
print(hash(obj2))    # Provides a hash value for obj2
