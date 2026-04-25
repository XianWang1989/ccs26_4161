
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return hash(id(self))  # using the object's id as the hash value

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will print: False
print(hash(obj1))    # This will print the hash value of obj1
