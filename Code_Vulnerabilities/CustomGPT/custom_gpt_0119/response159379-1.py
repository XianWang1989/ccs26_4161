
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Change this logic as needed

    def __hash__(self):
        return hash((self.__class__,))  # Use a unique hash value

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will call __eq__
print(hash(obj1))    # This will call __hash__
