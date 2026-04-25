
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Your actual equality logic here

    def __hash__(self):
        return hash(id(self))  # Returning the hash of the object itself for demonstration

# Example Usage
a = MyClass()
b = MyClass()
print(a == b)  # This will call __eq__
print(hash(a))  # This will call __hash__
