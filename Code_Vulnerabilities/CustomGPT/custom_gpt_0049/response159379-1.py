
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or provide a comparison for actual equality
        return False

    def __hash__(self):
        return hash(id(self))  # or an appropriate hash based on class attributes

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will return True based on the equality logic
print(hash(obj1))    # This will return a hash value without raising a warning
